src/processor/cancel.rs
=======================

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use super::*;

pub struct CancelArgs {
    pub keypair_path: Option<PathBuf>,
    pub rpc_url: Option<String>,
    pub proposal_id: Option<Pubkey>,
    pub latest: bool,
    pub mint_type: MintType,
}

pub fn cancel(args: CancelArgs) -> Result<()> {
    let config = config::CliConfig::new(args.keypair_path, args.rpc_url)?;

    let realm: RealmV2 = get_governance_state(&config.client, &config.realm_id)?;

    let governing_token_mint = match args.mint_type {
        MintType::Member => realm.community_mint,
        MintType::Council => realm
            .config
            .council_mint
            .ok_or_else(|| anyhow!("Council mint not found"))?,
    };

    let proposal_id = if args.latest {
        let governance: GovernanceV2 = get_governance_state(&config.client, &config.governance_id)?;
        let proposal_index = governance.proposals_count - 1;

        get_proposal_address(
            &GOVERNANCE_PROGRAM_ID,
            &config.governance_id,
            &governing_token_mint,
            &proposal_index.to_le_bytes(),
        )
    } else if let Some(proposal_id) = args.proposal_id {
        proposal_id
    } else {
        return Err(anyhow!("Either --latest or --proposal-id must be provided"));
    };

    let proposal_owner_record = get_token_owner_record_address(
        &GOVERNANCE_PROGRAM_ID,
        &config.realm_id,
        &governing_token_mint,
        &config.keypair.pubkey(),
    );

    let ix = cancel_proposal(
        &GOVERNANCE_PROGRAM_ID,
        &config.realm_id,
        &config.governance_id,
        &proposal_id,
        &proposal_owner_record,
        &config.keypair.pubkey(),
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


