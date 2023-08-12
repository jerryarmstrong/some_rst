src/processor/upgrade_program.rs
================================

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use super::*;

pub struct UpgradeProgramArgs {
    pub keypair_path: Option<PathBuf>,
    pub rpc_url: Option<String>,
    pub source_buffer: Pubkey,
    pub spill_account: Option<Pubkey>,
    pub name: String,
    pub description: String,
    pub mint_type: MintType,
    pub vote_type: VoteType,
    pub options: Vec<String>,
}

pub fn upgrade_program(args: UpgradeProgramArgs) -> Result<()> {
    let config = config::CliConfig::new(args.keypair_path, args.rpc_url)?;

    let realm = get_realm_data(&config.client, &config.realm_id)?;
    let governance = get_governance_data(&config.client, &config.governance_id)?;

    let governing_token_mint = match args.mint_type {
        MintType::Member => realm.community_mint,
        MintType::Council => realm
            .config
            .council_mint
            .ok_or_else(|| anyhow!("Council mint not found"))?,
    };

    debug!("Governing Token Mint: {governing_token_mint}");

    let proposal_index: u32 = governance.proposals_count;

    debug!("Proposal index: {proposal_index}");

    let proposal_owner_record = get_token_owner_record_address(
        &GOVERNANCE_PROGRAM_ID,
        &config.realm_id,
        &governing_token_mint,
        &config.keypair.pubkey(),
    );

    debug!("Proposal Owner Record: {proposal_owner_record}");

    let create_ix = create_proposal(
        &GOVERNANCE_PROGRAM_ID,
        &config.governance_id,
        &proposal_owner_record,
        &config.keypair.pubkey(),
        &config.keypair.pubkey(),
        None,
        &config.realm_id,
        args.name,
        args.description,
        &governing_token_mint,
        args.vote_type,
        args.options,
        true,
        proposal_index,
    );

    let proposal_address = get_proposal_address(
        &GOVERNANCE_PROGRAM_ID,
        &config.governance_id,
        &governing_token_mint,
        &proposal_index.to_le_bytes(),
    );

    debug!("Proposal Address: {proposal_address}");

    let token_owner_record = get_token_owner_record_address(
        &GOVERNANCE_PROGRAM_ID,
        &config.realm_id,
        &governing_token_mint,
        &config.keypair.pubkey(),
    );

    debug!("Token Owner Record: {token_owner_record}");

    let add_signatory_ix = add_signatory(
        &GOVERNANCE_PROGRAM_ID,
        &proposal_address,
        &token_owner_record,
        &config.keypair.pubkey(),
        &config.keypair.pubkey(),
        &config.keypair.pubkey(),
    );

    // Empirically determined from existing proposals. Not sure the significance of these yet.
    let option_index = 0;
    let index = 0;
    let hold_up_time = 0;

    let program_upgrade_instruction = create_upgrade_program_instruction(
        args.source_buffer,
        args.spill_account
            .unwrap_or_else(|| config.keypair.pubkey()),
        config.governance_id,
    )?;

    let insert_ix = insert_transaction(
        &GOVERNANCE_PROGRAM_ID,
        &config.governance_id,
        &proposal_address,
        &token_owner_record,
        &config.keypair.pubkey(),
        &config.keypair.pubkey(),
        option_index,
        index,
        hold_up_time,
        vec![program_upgrade_instruction],
    );

    let sign_off_ix = sign_off_proposal(
        &GOVERNANCE_PROGRAM_ID,
        &config.realm_id,
        &config.governance_id,
        &proposal_address,
        &config.keypair.pubkey(),
        None,
    );

    let tx = solana_sdk::transaction::Transaction::new_signed_with_payer(
        &[create_ix, add_signatory_ix, insert_ix, sign_off_ix],
        Some(&config.keypair.pubkey()),
        &[&config.keypair],
        config.client.get_latest_blockhash()?,
    );

    config
        .client
        .send_and_confirm_transaction_with_spinner(&tx)?;

    Ok(())
}


