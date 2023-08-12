src/processor/withdraw.rs
=========================

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use super::*;

pub struct WithdrawArgs {
    pub keypair_path: Option<PathBuf>,
    pub rpc_url: Option<String>,
    pub mint_type: MintType,
}

pub fn withdraw(args: WithdrawArgs) -> Result<()> {
    let config = config::CliConfig::new(args.keypair_path, args.rpc_url)?;

    let realm: RealmV2 = get_governance_state(&config.client, &config.realm_id)?;

    let governing_token_mint = match args.mint_type {
        MintType::Member => realm.community_mint,
        MintType::Council => realm
            .config
            .council_mint
            .ok_or_else(|| anyhow!("Council mint not found"))?,
    };

    debug!("Governing Token Mint: {governing_token_mint}");

    let governing_token_destination =
        get_associated_token_address(&config.keypair.pubkey(), &governing_token_mint);

    debug!("Governing Token Destination: {governing_token_destination}");

    let authority = config.keypair.pubkey();
    let governing_token_owner = &authority;

    let ix = withdraw_governing_tokens(
        &GOVERNANCE_PROGRAM_ID,
        &config.realm_id,
        &governing_token_destination,
        governing_token_owner,
        &governing_token_mint,
    );

    let tx = solana_sdk::transaction::Transaction::new_signed_with_payer(
        &[ix],
        Some(&config.keypair.pubkey()),
        &[&config.keypair],
        config.client.get_latest_blockhash()?,
    );

    config
        .client
        .send_and_confirm_transaction_with_spinner(&tx)?;

    Ok(())
}


