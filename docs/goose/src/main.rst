src/main.rs
===========

Last edited: 2023-06-13 21:53:04

Contents:

.. code-block:: rs

    use anyhow::Result;
use clap::Parser;

use goose::{
    args::{self, Commands},
    processor::*,
};

#[tokio::main]
async fn main() -> Result<()> {
    solana_logger::setup_with_default("solana=error");

    let args = args::Args::parse();

    let keypair_path = args.keypair_path.clone();
    let rpc_url = args.rpc_url.clone();

    match args.command {
        Commands::Init {
            collection_mint,
            unlock_method,
            size,
        } => process_initialize(keypair_path, rpc_url, collection_mint, unlock_method, size),
        Commands::InitMsg {
            payer,
            authority,
            collection_mint,
            unlock_method,
            size,
        } => process_initialize_msg(payer, authority, collection_mint, unlock_method, size),
        Commands::InitSigner => process_initialize_signer(keypair_path, rpc_url),
        Commands::Cancel { collection_mint } => {
            process_close(keypair_path, rpc_url, collection_mint)
        }
        Commands::GetState { collection_mint } => {
            process_get_state(keypair_path, rpc_url, collection_mint)
        }
        Commands::GetAllStates => process_get_all_states(keypair_path, rpc_url),
        Commands::Update {
            collection_mint,
            rule_set,
            size,
            new_update_authority,
        } => process_update(
            keypair_path,
            rpc_url,
            collection_mint,
            rule_set,
            size,
            new_update_authority,
        ),
        Commands::UpdateMsg {
            collection_mint,
            rule_set,
            size,
            new_update_authority,
            authority_pubkey,
        } => process_update_msg(
            keypair_path,
            rpc_url,
            collection_mint,
            rule_set,
            size,
            new_update_authority,
            authority_pubkey,
        ),
        Commands::Start { collection_mint } => {
            process_start(keypair_path, rpc_url, collection_mint)
        }
        Commands::Migrate {
            collection_mint,
            mint_list,
            batch_size,
        } => {
            process_migrate(
                keypair_path,
                rpc_url,
                collection_mint,
                mint_list,
                batch_size,
            )
            .await
        }
        Commands::Check {
            mint_list,
            batch_size,
        } => process_check(keypair_path, rpc_url, mint_list, batch_size).await,
    }
}


