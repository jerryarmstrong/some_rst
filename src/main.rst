src/main.rs
===========

Last edited: 2021-09-02 06:22:54

Contents:

.. code-block:: rs

    use {
    clap::{Arg, ArgMatches},
    inc_20210825::{audit, cleanup},
    solana_clap_utils::{
        input_validators::{
            is_url_or_moniker, is_valid_pubkey, is_valid_signer, normalize_to_url_if_moniker,
        },
        keypair::{signer_from_path, signer_from_path_with_config, SignerFromPathConfig},
    },
    solana_client::rpc_client::RpcClient,
    solana_remote_wallet::remote_wallet::RemoteWalletManager,
    solana_sdk::{
        commitment_config::CommitmentConfig, program_pack::Pack, pubkey::Pubkey, signature::Signer,
        system_program,
    },
    std::{process::exit, sync::Arc},
};

pub fn owner_keypair_arg<'a, 'b>() -> Arg<'a, 'b> {
    Arg::with_name("owner")
        .value_name("OWNER_KEYPAIR")
        .validator(is_valid_signer)
        .required(true)
        .multiple(true)
        .help("Keypair or address of the token's owner")
}

pub fn mint_address_arg<'a, 'b>() -> Arg<'a, 'b> {
    Arg::with_name("mint")
        .long("mint")
        .takes_value(true)
        .value_name("MINT_ADDRESS")
        .multiple(true)
        .number_of_values(1)
        .validator(is_valid_pubkey)
        .help("Address of the SPL token mint")
}

fn get_signer(
    matches: &ArgMatches<'_>,
    keypair_path: &str,
    wallet_manager: &mut Option<Arc<RemoteWalletManager>>,
    allow_null_signer: bool,
) -> Box<dyn Signer> {
    let config = SignerFromPathConfig { allow_null_signer };
    signer_from_path_with_config(matches, keypair_path, "owner", wallet_manager, &config)
        .unwrap_or_else(|e| {
            eprintln!("error: {}", e);
            exit(1);
        })
}

fn get_owners_and_mints(
    sub_matches: &ArgMatches<'_>,
    allow_null_signer: bool,
    rpc_client: &RpcClient,
    wallet_manager: &mut Option<Arc<RemoteWalletManager>>,
) -> (Vec<Box<dyn Signer>>, Option<Vec<Pubkey>>) {
    let mints = if sub_matches.is_present("mint") {
        let mints = sub_matches
            .values_of("mint")
            .unwrap()
            .map(|p| {
                get_signer(
                    sub_matches,
                    p,
                    wallet_manager,
                    /* allow_null_signer = */ true,
                )
                .pubkey()
            })
            .collect::<Vec<_>>();
        for mint in &mints {
            let mint_account = rpc_client.get_account(mint).unwrap_or_else(|_| {
                eprintln!(
                    "Account {} expected to be an SPL token mint, but does not exist. Maybe this is a system account?",
                    mint
                );
                exit(1);
            });
            if mint_account.owner != spl_token::id() {
                eprintln!("Account {} is not owned by the SPL token program, actually owned by {}, likely this parameter is incorrect", mint, mint_account.owner);
                exit(1);
            }
            let _ = spl_token::state::Mint::unpack(&mint_account.data).unwrap_or_else(|_| {
                eprintln!(
                    "Account {} is not an SPL token mint, likely this parameter is incorrect",
                    mint
                );
                exit(1);
            });
        }
        Some(mints)
    } else {
        None
    };

    let owners = sub_matches
        .values_of("owner")
        .unwrap()
        .map(|p| get_signer(sub_matches, p, wallet_manager, allow_null_signer))
        .collect::<Vec<_>>();

    for owner in &owners {
        let owner_address = owner.pubkey();
        // Don't unwrap to allow possibly non-existent owner
        // A non-existent owner just means a system account with no lamports,
        // which is a valid sitation for an owner account.
        if let Ok(owner_account) = rpc_client.get_account(&owner_address) {
            if owner_account.owner == spl_token::id() {
                eprintln!("Account {} is not owned by the system program, actually owned by the SPL token program. Maybe this is a mint?", &owner_address);
                exit(1);
            } else if owner_account.owner != system_program::id() {
                eprintln!("Account {} is not owned by the system program, actually owned by {}, this parameter is likely incorrect", &owner_address, owner_account.owner);
                exit(1);
            }
        }
    }

    (owners, mints)
}

fn check_rpc_has_genesis_block(rpc_client: &RpcClient, rpc_url: &str) {
    let rpc_first_slot = rpc_client.get_first_available_block().unwrap_or_else(|_| {
        eprintln!("Could not fetch available block from {}, perhaps the URL is wrong or the backend is down", rpc_url);
        exit(1);
    });
    const FIRST_SLOT: u64 = 1; // solana-test-validator starts at slot 1, so this makes testing easier
    if rpc_first_slot > FIRST_SLOT {
        eprintln!(
            "Earliest block from {} is {}, some transactions will be omitted during audit",
            rpc_url, rpc_first_slot
        );
        exit(1);
    }
}

fn main() {
    let matches = clap::App::new("inc-20210805")
        .setting(clap::AppSettings::SubcommandRequiredElseHelp)
        .arg({
            let arg = Arg::with_name("config_file")
                .short("C")
                .long("config")
                .value_name("PATH")
                .takes_value(true)
                .global(true)
                .help("Configuration file to use");
            if let Some(ref config_file) = *solana_cli_config::CONFIG_FILE {
                arg.default_value(config_file)
            } else {
                arg
            }
        })
        .arg(
            Arg::with_name("verbose")
                .short("v")
                .long("verbose")
                .takes_value(false)
                .global(true)
                .help("Show additional information"),
        )
        .arg(
            Arg::with_name("dry_run")
                .long("dry-run")
                .takes_value(false)
                .global(true)
                .help("Do all processing without sending transactions"),
        )
        .arg(
            Arg::with_name("skip_genesis_block_check")
                .long("skip-genesis-block-check")
                .takes_value(false)
                .global(true)
                .help("Skip checking that the RPC endpoint has the genesis block"),
        )
        .arg(
            Arg::with_name("json_rpc_url")
                .short("u")
                .long("url")
                .value_name("URL_OR_MONIKER")
                .takes_value(true)
                .global(true)
                .validator(is_url_or_moniker)
                .help(
                    "URL for Solana's JSON RPC or moniker (or their first letter): \
                       [mainnet-beta, testnet, devnet, localhost] \
                    Default from the configuration file.",
                ),
        )
        .subcommand(
            clap::SubCommand::with_name("audit")
                .about("Audit all accounts for the owners on the given mints")
                .arg(mint_address_arg())
                .arg(owner_keypair_arg()),
        )
        .subcommand(
            clap::SubCommand::with_name("cleanup")
                .about("Revoke all account delegations for the owners on the given mints")
                .arg(mint_address_arg())
                .arg(owner_keypair_arg()),
        )
        .get_matches();

    let mut wallet_manager = None;
    let dry_run = matches.is_present("dry_run");
    let config = {
        let cli_config = if let Some(config_file) = matches.value_of("config_file") {
            solana_cli_config::Config::load(config_file).unwrap_or_default()
        } else {
            solana_cli_config::Config::default()
        };
        let json_rpc_url = normalize_to_url_if_moniker(
            matches
                .value_of("json_rpc_url")
                .unwrap_or(&cli_config.json_rpc_url),
        );

        let fee_payer = signer_from_path(
            &matches,
            matches
                .value_of("fee_payer")
                .unwrap_or(&cli_config.keypair_path),
            "fee_payer",
            &mut wallet_manager,
        )
        .unwrap_or_else(|e| {
            eprintln!("error: {}", e);
            exit(1);
        });

        let rpc_client =
            RpcClient::new_with_commitment(json_rpc_url.clone(), CommitmentConfig::confirmed());

        inc_20210825::config::Config {
            json_rpc_url,
            rpc_client,
            fee_payer,
            dry_run,
            verbose: matches.is_present("verbose"),
        }
    };

    match matches.subcommand() {
        ("audit", Some(sub_matches)) => {
            let (owners, mints) =
                get_owners_and_mints(sub_matches, true, &config.rpc_client, &mut wallet_manager);
            if !matches.is_present("skip_genesis_block_check") {
                check_rpc_has_genesis_block(&config.rpc_client, &config.json_rpc_url);
            }

            audit::run(config, owners, mints);
        }
        ("cleanup", Some(sub_matches)) => {
            let allow_null_signer = dry_run;
            let (owners, mints) = get_owners_and_mints(
                sub_matches,
                allow_null_signer,
                &config.rpc_client,
                &mut wallet_manager,
            );
            cleanup::run(config, owners, mints);
        }
        _ => unreachable!(),
    }
}


