src/processor.rs
================

Last edited: 2023-06-13 21:53:04

Contents:

.. code-block:: rs

    use std::{fs::File, path::PathBuf, str::FromStr, sync::Arc};

use ::futures::stream::FuturesUnordered;
use anyhow::Result;
use borsh::BorshDeserialize;
use console::style;
use futures::StreamExt;
use mpl_migration_validator::{
    state::{MigrationState, UnlockMethod},
    utils::find_migration_state_pda,
    PROGRAM_SIGNER,
};
use mpl_token_metadata::{
    pda::find_metadata_account,
    state::{Metadata, TokenMetadataAccount, TokenStandard},
};
use serde::{Deserialize, Serialize};
use solana_client::rpc_client::RpcClient;
use solana_program::{
    bpf_loader_upgradeable::UpgradeableLoaderState, program_pack::Pack, pubkey::Pubkey,
};
use solana_sdk::{
    signature::{Keypair, Signature},
    signer::Signer,
    transaction::Transaction,
};
use spl_token::state::Account as TokenAccount;
use tokio::sync::{Mutex, Semaphore};

use crate::{
    methods::{
        close, get_state, initialize, initialize_msg, migrate_item, start, update, update_msg,
        CloseParams, GetStateParams, InitializeMsgParams, InitializeParams, MigrateParams,
        StartParams, UpdateMsgParams, UpdateParams,
    },
    setup,
    utils::{create_progress_bar, get_cluster, get_nft_token_account, spinner_with_style},
};

pub fn process_initialize(
    keypair: Option<PathBuf>,
    rpc_url: Option<String>,
    collection_mint: Pubkey,
    unlock_method: String,
    collection_size: u32,
) -> Result<()> {
    let config = setup::CliConfig::new(keypair, rpc_url)?;

    let unlock_method = match unlock_method.to_lowercase().as_str() {
        "timed" => UnlockMethod::Timed,
        "vote" => UnlockMethod::Vote,
        _ => {
            return Err(anyhow::anyhow!(
                "Invalid unlock method. Must be one of: Timed, Vote"
            ))
        }
    };

    let params = InitializeParams {
        client: &config.client,
        payer: &config.keypair,
        authority: &config.keypair,
        rule_set: None,
        collection_mint,
        unlock_method,
        collection_size,
    };
    let spinner = spinner_with_style();
    spinner.set_message("Initializing migration state...");
    let sig = initialize(params)?;
    spinner.finish();

    let cluster = get_cluster(&config.client)?;
    let link = format!("https://explorer.solana.com/tx/{sig}?cluster={cluster}");
    println!(
        "Intialized migration state successfully in tx: {}",
        style(link).green()
    );

    // Delay before fetching the state.
    let spinner = spinner_with_style();
    spinner.set_message("Waiting for migration state to be initialized...");
    std::thread::sleep(std::time::Duration::from_secs(3));
    spinner.finish();

    let get_state_params = GetStateParams {
        client: &config.client,
        collection_mint,
    };
    spinner.set_message("Fetching migration state...");
    let state = get_state(get_state_params)?;
    spinner.finish();

    println!("Migration state:\n {:#?}", style(state).green());

    Ok(())
}

pub fn process_initialize_msg(
    payer: Pubkey,
    authority: Pubkey,
    collection_mint: Pubkey,
    unlock_method: String,
    collection_size: u32,
) -> Result<()> {
    let unlock_method = match unlock_method.to_lowercase().as_str() {
        "timed" => UnlockMethod::Timed,
        "vote" => UnlockMethod::Vote,
        _ => {
            return Err(anyhow::anyhow!(
                "Invalid unlock method. Must be one of: Timed, Vote"
            ))
        }
    };

    let params = InitializeMsgParams {
        payer,
        authority,
        rule_set: None,
        collection_mint,
        unlock_method,
        collection_size,
    };
    let spinner = spinner_with_style();
    spinner.set_message("Initializing migration state...");
    let message = initialize_msg(params)?;
    spinner.finish();

    println!("Transaction message:\n {:#?}", style(message).green());

    Ok(())
}

pub fn process_initialize_signer(keypair: Option<PathBuf>, rpc_url: Option<String>) -> Result<()> {
    let config = setup::CliConfig::new(keypair, rpc_url)?;

    let instruction = mpl_migration_validator::instruction::init_signer(config.keypair.pubkey());
    let spinner = spinner_with_style();
    spinner.set_message("Initializing program signer...");
    let recent_blockhash = config.client.get_latest_blockhash()?;

    let transaction = Transaction::new_signed_with_payer(
        &[instruction],
        Some(&config.keypair.pubkey()),
        &[&config.keypair],
        recent_blockhash,
    );

    let sig = config.client.send_and_confirm_transaction(&transaction)?;
    spinner.finish();
    println!(
        "Initialized program signer successfully in tx: {}",
        style(sig).green()
    );

    Ok(())
}

pub fn process_close(
    keypair: Option<PathBuf>,
    rpc_url: Option<String>,
    collection_mint: Pubkey,
) -> Result<()> {
    let config = setup::CliConfig::new(keypair, rpc_url)?;

    let params = CloseParams {
        client: &config.client,
        authority: &config.keypair,
        collection_mint,
    };
    let spinner = spinner_with_style();
    spinner.set_message("Canceling migration...");
    let sig = close(params)?;
    spinner.finish();

    let cluster = get_cluster(&config.client)?;
    let link = format!("https://explorer.solana.com/tx/{sig}?cluster={cluster}");
    println!(
        "Canceled migration successfully in tx: {}",
        style(link).green()
    );

    Ok(())
}

pub fn process_get_state(
    keypair: Option<PathBuf>,
    rpc_url: Option<String>,
    collection_mint: Pubkey,
) -> Result<()> {
    let config = setup::CliConfig::new(keypair, rpc_url)?;

    let get_state_params = GetStateParams {
        client: &config.client,
        collection_mint,
    };
    let state = get_state(get_state_params)?;

    println!("Migration state:\n {:#?}", style(state).green());

    Ok(())
}

pub fn process_get_all_states(keypair: Option<PathBuf>, rpc_url: Option<String>) -> Result<()> {
    let config = setup::CliConfig::new(keypair, rpc_url)?;

    // Get all the program accounts for mpl-migration-validator.
    let account_results = config
        .client
        .get_program_accounts(&mpl_migration_validator::ID)?;

    let cluster = get_cluster(&config.client)?;

    println!(
        "Found: {}",
        style(format!("{} states", account_results.len() - 1)).green()
    );

    let file_name = format!("{cluster}_migration_states.json");

    let mut states = Vec::new();

    for (pubkey, account) in account_results {
        // Skip program signer account
        if pubkey == PROGRAM_SIGNER {
            continue;
        }

        let state =
            match <MigrationState as BorshDeserialize>::deserialize(&mut account.data.as_slice()) {
                Ok(state) => state,
                Err(_) => {
                    println!("Failed to deserialize state for account {pubkey:?}");
                    continue;
                }
            };
        states.push(state);
    }

    let f = File::create(&file_name)?;
    serde_json::to_writer_pretty(f, &states)?;

    println!(
        "{}",
        style(format!("Wrote migration states to {file_name}")).green()
    );

    Ok(())
}

pub fn process_update(
    keypair: Option<PathBuf>,
    rpc_url: Option<String>,
    collection_mint: Pubkey,
    rule_set: Option<Pubkey>,
    collection_size: Option<u32>,
    new_update_authority: Option<Pubkey>,
) -> Result<()> {
    let config = setup::CliConfig::new(keypair, rpc_url)?;

    let (migration_state, _) = find_migration_state_pda(&collection_mint);

    let params = UpdateParams {
        client: &config.client,
        authority: &config.keypair,
        migration_state,
        collection_size,
        rule_set,
        new_update_authority,
    };
    let spinner = spinner_with_style();
    spinner.set_message("Updating migration state...");
    let sig = update(params)?;
    spinner.finish();

    let cluster = get_cluster(&config.client)?;
    let link = format!("https://explorer.solana.com/tx/{sig}?cluster={cluster}");
    println!(
        "Updated migration state successfully in tx: {}",
        style(link).green()
    );

    Ok(())
}

pub fn process_update_msg(
    keypair: Option<PathBuf>,
    rpc_url: Option<String>,
    collection_mint: Pubkey,
    rule_set: Option<Pubkey>,
    collection_size: Option<u32>,
    new_update_authority: Option<Pubkey>,
    authority_pubkey: Pubkey,
) -> Result<()> {
    let config = setup::CliConfig::new(keypair, rpc_url)?;

    let (migration_state, _) = find_migration_state_pda(&collection_mint);

    let params = UpdateMsgParams {
        authority: &config.keypair,
        authority_pubkey,
        migration_state,
        collection_size,
        rule_set,
        new_update_authority,
    };
    let spinner = spinner_with_style();
    spinner.set_message("Updating migration state...");
    let tx = update_msg(params)?;
    spinner.finish();

    println!("Transaction: {}", style(tx).green());

    Ok(())
}

pub fn process_start(
    keypair: Option<PathBuf>,
    rpc_url: Option<String>,
    collection_mint: Pubkey,
) -> Result<()> {
    let config = setup::CliConfig::new(keypair, rpc_url)?;

    let params = StartParams {
        client: &config.client,
        authority: &config.keypair,
        collection_mint,
    };

    let spinner = spinner_with_style();
    spinner.set_message("Enabling migration...");
    let sig = start(params)?;
    spinner.finish();

    let cluster = get_cluster(&config.client)?;
    let link = format!("https://explorer.solana.com/tx/{sig}?cluster={cluster}");
    println!(
        "Started migration successfully in tx: {}",
        style(link).green()
    );

    Ok(())
}

#[derive(Serialize, Deserialize, Debug)]
pub struct MigratedMint {
    sig: String,
    item_mint: String,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct MigrationError {
    mint: String,
    error: String,
}

pub async fn process_migrate(
    keypair: Option<PathBuf>,
    rpc_url: Option<String>,
    collection_mint: Pubkey,
    mint_list: PathBuf,
    batch_size: usize,
) -> Result<()> {
    let config = setup::CliConfig::new(keypair, rpc_url)?;

    let f = File::open(mint_list)?;
    let mints: Vec<String> = serde_json::from_reader(f)?;
    let mints: Vec<Pubkey> = mints
        .into_iter()
        .map(|s| Pubkey::from_str(&s).unwrap())
        .collect();

    let migrate_state = get_state(GetStateParams {
        client: &config.client,
        collection_mint,
    })?;

    let rule_set = migrate_state.collection_info.rule_set;

    let completed_mints: Arc<Mutex<Vec<MigratedMint>>> = Arc::new(Mutex::new(Vec::new()));
    let errors: Arc<Mutex<Vec<MigrationError>>> = Arc::new(Mutex::new(Vec::new()));

    let keypair = Arc::new(config.keypair);
    let client = Arc::new(config.client);

    let mut tasks = FuturesUnordered::new();
    let semaphore = Arc::new(Semaphore::new(batch_size));
    let pb = create_progress_bar("", mints.len() as u64);

    pb.set_message("Migrating mints...");
    for item_mint in mints {
        let permit = Arc::clone(&semaphore).acquire_owned().await.unwrap();
        let pb = pb.clone();
        let completed_mints = completed_mints.clone();
        let errors = errors.clone();
        let keypair = keypair.clone();
        let client = client.clone();

        tasks.push(tokio::spawn(async move {
            let _permit = permit;

            let args = MigrateArgs {
                keypair,
                client,
                collection_mint,
                item_mint,
                rule_set,
            };
            match migrate_mint(args).await {
                Ok(sig) => {
                    completed_mints.lock().await.push(MigratedMint {
                        sig: sig.to_string(),
                        item_mint: item_mint.to_string(),
                    });
                }
                Err(e) => {
                    errors.lock().await.push(MigrationError {
                        mint: item_mint.to_string(),
                        error: e.to_string(),
                    });
                }
            }

            pb.inc(1);
        }));
    }

    while let Some(task) = tasks.next().await {
        task?;
    }

    let completed_mints = Arc::try_unwrap(completed_mints).unwrap().into_inner();
    let errors = Arc::try_unwrap(errors).unwrap().into_inner();

    println!("Migrated {} mints", completed_mints.len());
    println!("Failed to migrate {} mints", errors.len());

    let success_name = format!("{collection_mint}_migrated_mints.json");
    let failures_name = format!("{collection_mint}_failed_mints.json");
    let f = File::create(success_name)?;
    let e = File::create(failures_name)?;
    serde_json::to_writer_pretty(f, &completed_mints)?;
    serde_json::to_writer_pretty(e, &errors)?;

    Ok(())
}

struct MigrateArgs {
    keypair: Arc<Keypair>,
    client: Arc<RpcClient>,
    collection_mint: Pubkey,
    item_mint: Pubkey,
    rule_set: Pubkey,
}

async fn migrate_mint(args: MigrateArgs) -> Result<Signature> {
    let item_token = get_nft_token_account(&args.client, args.item_mint)?;

    let account = args.client.get_account(&item_token)?;

    let token_account = TokenAccount::unpack(&account.data)?;

    let token_owner = token_account.owner;
    let token_owner_program = args.client.get_account(&token_owner)?.owner;

    let token_owner_program_account = args.client.get_account(&token_owner_program)?;

    // We need to pass the program data buffer to the migration program
    // if the token owner program is an upgradeable program.
    let state_opt: Option<UpgradeableLoaderState> =
        bincode::deserialize(&token_owner_program_account.data).ok();

    let token_owner_program_buffer = if let Some(state) = state_opt {
        match state {
            UpgradeableLoaderState::Program {
                programdata_address,
            } => Some(programdata_address),
            _ => None,
        }
    } else {
        None
    };

    let params = MigrateParams {
        client: &args.client,
        payer: &args.keypair,
        item_mint: args.item_mint,
        item_token,
        token_owner,
        token_owner_program,
        token_owner_program_buffer,
        collection_mint: args.collection_mint,
        rule_set: args.rule_set,
    };

    migrate_item(params)
}

pub async fn process_check(
    keypair: Option<PathBuf>,
    rpc_url: Option<String>,
    mint_list: PathBuf,
    batch_size: usize,
) -> Result<()> {
    let config = setup::CliConfig::new(keypair, rpc_url)?;

    let f = File::open(mint_list)?;
    let mints: Vec<String> = serde_json::from_reader(f)?;
    let mints: Vec<Pubkey> = mints
        .into_iter()
        .map(|s| Pubkey::from_str(&s).unwrap())
        .collect();

    let completed_mints: Arc<Mutex<Vec<String>>> = Arc::new(Mutex::new(Vec::new()));
    let unmigrated_mints: Arc<Mutex<Vec<String>>> = Arc::new(Mutex::new(Vec::new()));
    let errors: Arc<Mutex<Vec<MigrationError>>> = Arc::new(Mutex::new(Vec::new()));

    let client = Arc::new(config.client);

    let mut tasks = FuturesUnordered::new();
    let semaphore = Arc::new(Semaphore::new(batch_size));
    let pb = create_progress_bar("", mints.len() as u64);

    pb.set_message("Checking mints...");
    for item_mint in mints {
        let permit = Arc::clone(&semaphore).acquire_owned().await.unwrap();
        let pb = pb.clone();
        let completed_mints = completed_mints.clone();
        let unmigrated_mints = unmigrated_mints.clone();
        let errors = errors.clone();
        let client = client.clone();

        tasks.push(tokio::spawn(async move {
            let _permit = permit;

            let (metadata, _) = find_metadata_account(&item_mint);

            let account = match client.get_account_data(&metadata) {
                Ok(account) => account,
                Err(e) => {
                    errors.lock().await.push(MigrationError {
                        mint: item_mint.to_string(),
                        error: e.to_string(),
                    });
                    pb.inc(1);
                    return;
                }
            };

            let md = match Metadata::safe_deserialize(&account) {
                Ok(md) => md,
                Err(e) => {
                    errors.lock().await.push(MigrationError {
                        mint: item_mint.to_string(),
                        error: e.to_string(),
                    });
                    pb.inc(1);
                    return;
                }
            };

            if let Some(token_standard) = md.token_standard {
                if token_standard == TokenStandard::ProgrammableNonFungible {
                    completed_mints.lock().await.push(item_mint.to_string());
                } else {
                    unmigrated_mints.lock().await.push(item_mint.to_string());
                }
            } else {
                unmigrated_mints.lock().await.push(item_mint.to_string());
            }

            pb.inc(1);
        }));
    }

    while let Some(task) = tasks.next().await {
        task?;
    }

    let completed_mints = Arc::try_unwrap(completed_mints).unwrap().into_inner();
    let unmigrated_mints = Arc::try_unwrap(unmigrated_mints).unwrap().into_inner();
    let errors = Arc::try_unwrap(errors).unwrap().into_inner();

    println!("Migrated {} mints", completed_mints.len());
    println!("Unmigrated {} mints", unmigrated_mints.len());
    println!("Encountered {} errors", errors.len());

    let migrated_name = "migrated_mints.json".to_string();
    let unmigrated_name = "unmigrated_mints.json".to_string();
    let errors_name = "errors.json".to_string();

    let m = File::create(migrated_name)?;
    let u = File::create(unmigrated_name)?;
    let e = File::create(errors_name)?;

    serde_json::to_writer_pretty(m, &completed_mints)?;
    serde_json::to_writer_pretty(u, &unmigrated_mints)?;
    serde_json::to_writer_pretty(e, &errors)?;

    Ok(())
}


