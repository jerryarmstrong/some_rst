src/methods.rs
==============

Last edited: 2023-06-13 21:53:04

Contents:

.. code-block:: rs

    use anyhow::Result;
use borsh::BorshDeserialize;
use mpl_migration_validator::{
    instruction::{InitializeArgs, UpdateArgs},
    state::{MigrationState, UnlockMethod},
};
use solana_client::rpc_client::RpcClient;
use solana_program::{message::Message, pubkey::Pubkey};
use solana_sdk::{
    signature::{Keypair, Signature, Signer},
    transaction::Transaction,
};

use crate::utils::find_migrate_state_pda;

pub struct InitializeParams<'a> {
    pub client: &'a RpcClient,
    pub payer: &'a Keypair,
    pub authority: &'a Keypair,
    pub rule_set: Option<Pubkey>,
    pub collection_mint: Pubkey,
    pub unlock_method: UnlockMethod,
    pub collection_size: u32,
}

pub fn initialize(params: InitializeParams) -> Result<Signature> {
    let InitializeParams {
        client,
        payer,
        authority,
        rule_set,
        collection_mint,
        unlock_method,
        collection_size,
    } = params;

    let args = InitializeArgs {
        rule_set: Some(rule_set.unwrap_or_default()),
        unlock_method,
        collection_size,
    };

    let instruction = mpl_migration_validator::instruction::initialize(
        payer.pubkey(),
        authority.pubkey(),
        collection_mint,
        args,
    );

    let recent_blockhash = client.get_latest_blockhash()?;

    let transaction = Transaction::new_signed_with_payer(
        &[instruction],
        Some(&payer.pubkey()),
        &[payer, authority],
        recent_blockhash,
    );

    let sig = client.send_and_confirm_transaction(&transaction)?;

    Ok(sig)
}

pub struct InitializeMsgParams {
    pub payer: Pubkey,
    pub authority: Pubkey,
    pub rule_set: Option<Pubkey>,
    pub collection_mint: Pubkey,
    pub unlock_method: UnlockMethod,
    pub collection_size: u32,
}

pub fn initialize_msg(params: InitializeMsgParams) -> Result<String> {
    let InitializeMsgParams {
        payer,
        authority,
        rule_set,
        collection_mint,
        unlock_method,
        collection_size,
    } = params;

    let args = InitializeArgs {
        rule_set: Some(rule_set.unwrap_or_default()),
        unlock_method,
        collection_size,
    };

    let instruction =
        mpl_migration_validator::instruction::initialize(payer, authority, collection_mint, args);

    let message = Message::new(&[instruction], Some(&payer));
    Ok(bs58::encode(message.serialize()).into_string())
}

pub struct CloseParams<'a> {
    pub client: &'a RpcClient,
    pub authority: &'a Keypair,
    pub collection_mint: Pubkey,
}

pub fn close(params: CloseParams) -> Result<Signature> {
    let CloseParams {
        client,
        authority,
        collection_mint,
    } = params;

    let migrate_state_pubkey = find_migrate_state_pda(&collection_mint).0;

    let instruction =
        mpl_migration_validator::instruction::close(authority.pubkey(), migrate_state_pubkey);

    let recent_blockhash = client.get_latest_blockhash()?;

    let transaction = Transaction::new_signed_with_payer(
        &[instruction],
        Some(&authority.pubkey()),
        &[authority],
        recent_blockhash,
    );

    let sig = client.send_and_confirm_transaction(&transaction)?;

    Ok(sig)
}

pub struct UpdateParams<'a> {
    pub client: &'a RpcClient,
    pub authority: &'a Keypair,
    pub migration_state: Pubkey,
    pub rule_set: Option<Pubkey>,
    pub collection_size: Option<u32>,
    pub new_update_authority: Option<Pubkey>,
}

pub fn update(params: UpdateParams) -> Result<Signature> {
    let UpdateParams {
        client,
        authority,
        migration_state,
        rule_set,
        collection_size,
        new_update_authority,
    } = params;

    let args = UpdateArgs {
        rule_set,
        collection_size,
        new_update_authority,
    };

    let instruction =
        mpl_migration_validator::instruction::update(authority.pubkey(), migration_state, args);

    let recent_blockhash = client.get_latest_blockhash()?;

    let transaction = Transaction::new_signed_with_payer(
        &[instruction],
        Some(&authority.pubkey()),
        &[authority],
        recent_blockhash,
    );

    let sig = client.send_and_confirm_transaction(&transaction)?;

    Ok(sig)
}

pub struct UpdateMsgParams<'a> {
    pub authority: &'a Keypair,
    pub authority_pubkey: Pubkey,
    pub migration_state: Pubkey,
    pub rule_set: Option<Pubkey>,
    pub collection_size: Option<u32>,
    pub new_update_authority: Option<Pubkey>,
}

pub fn update_msg(params: UpdateMsgParams) -> Result<String> {
    let UpdateMsgParams {
        authority,
        authority_pubkey,
        migration_state,
        rule_set,
        collection_size,
        new_update_authority,
    } = params;

    let args = UpdateArgs {
        rule_set,
        collection_size,
        new_update_authority,
    };

    let instruction =
        mpl_migration_validator::instruction::update(authority_pubkey, migration_state, args);

    let message = Message::new(&[instruction], Some(&authority.pubkey()));
    Ok(bs58::encode(message.serialize()).into_string())
}

pub struct StartParams<'a> {
    pub client: &'a RpcClient,
    pub authority: &'a Keypair,
    pub collection_mint: Pubkey,
}

pub fn start(params: StartParams) -> Result<Signature> {
    let StartParams {
        client,
        authority,
        collection_mint,
    } = params;

    let instruction = mpl_migration_validator::instruction::start(
        authority.pubkey(),
        authority.pubkey(),
        collection_mint,
    );

    let recent_blockhash = client.get_latest_blockhash()?;

    let transaction = Transaction::new_signed_with_payer(
        &[instruction],
        Some(&authority.pubkey()),
        &[authority],
        recent_blockhash,
    );

    let sig = client.send_and_confirm_transaction(&transaction)?;

    Ok(sig)
}

pub struct GetStateParams<'a> {
    pub client: &'a RpcClient,
    pub collection_mint: Pubkey,
}

pub fn get_state(params: GetStateParams) -> Result<MigrationState> {
    let GetStateParams {
        client,
        collection_mint,
    } = params;

    let pubkey = find_migrate_state_pda(&collection_mint).0;

    let account = client.get_account_data(&pubkey)?;

    let state = MigrationState::deserialize(&mut account.as_slice())?;

    Ok(state)
}

pub struct MigrateParams<'a> {
    pub client: &'a RpcClient,
    pub payer: &'a Keypair,
    pub item_mint: Pubkey,
    pub item_token: Pubkey,
    pub token_owner: Pubkey,
    pub token_owner_program: Pubkey,
    pub token_owner_program_buffer: Option<Pubkey>,
    pub collection_mint: Pubkey,
    pub rule_set: Pubkey,
}

pub fn migrate_item(params: MigrateParams) -> Result<Signature> {
    let MigrateParams {
        client,
        payer,
        item_mint,
        item_token,
        token_owner,
        token_owner_program,
        token_owner_program_buffer,
        collection_mint,
        rule_set,
    } = params;

    let instruction = mpl_migration_validator::instruction::migrate_item(
        payer.pubkey(),
        item_mint,
        item_token,
        token_owner,
        token_owner_program,
        token_owner_program_buffer,
        collection_mint,
        rule_set,
    );

    let recent_blockhash = client.get_latest_blockhash()?;

    let transaction = Transaction::new_signed_with_payer(
        &[instruction],
        Some(&payer.pubkey()),
        &[payer],
        recent_blockhash,
    );

    let sig = client.send_and_confirm_transaction(&transaction)?;

    Ok(sig)
}


