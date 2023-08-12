src/processor/execute.rs
========================

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use super::*;

pub struct ExecuteArgs {
    pub keypair_path: Option<PathBuf>,
    pub rpc_url: Option<String>,
    pub proposal_id: Option<Pubkey>,
    pub latest: bool,
    pub mint_type: MintType,
}

pub fn execute(args: ExecuteArgs) -> Result<()> {
    let config = config::CliConfig::new(args.keypair_path, args.rpc_url)?;

    let realm: RealmV2 = get_governance_state(&config.client, &config.realm_id)?;

    let governing_token_mint = match args.mint_type {
        MintType::Member => realm.community_mint,
        MintType::Council => realm
            .config
            .council_mint
            .ok_or_else(|| anyhow!("Council mint not found"))?,
    };

    debug!("Governing token mint: {governing_token_mint}");

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

    debug!("Proposal ID: {proposal_id}");

    // We need to find the owner of the proposal to find the correct proposal_owner_record
    // as this will only be the voter if the voter also created the proposal.

    let proposal: ProposalV2 = get_governance_state(&config.client, &proposal_id)?;

    // All our upgrade proposals should have option and instruction indexes of 0,
    // but to support more generically we should get the indexes.

    let option_index = (proposal
        .options
        .first()
        .expect("More than one proposal option found!")
        .transactions_next_index
        - 1) as u8;

    debug!("Option index: {option_index}");

    let proposal_transaction_pubkey = get_proposal_transaction_address(
        &GOVERNANCE_PROGRAM_ID,
        &proposal_id,
        &option_index.to_le_bytes(),
        &[0, 0],
    );

    debug!("Proposal transaction pubkey: {proposal_transaction_pubkey}");

    let proposal_transaction: ProposalTransactionV2 =
        get_governance_state(&config.client, &proposal_transaction_pubkey)?;

    if proposal_transaction.instructions.len() > 1 {
        return Err(anyhow!(
            "More than one instruction found in proposal transaction"
        ));
    }
    let instruction = proposal_transaction
        .instructions
        .first()
        .expect("No instructions found in proposal transaction");

    let instruction_program_id = instruction.program_id;

    // Convert from the SPL governance type to the Solana SDK type
    // Manually set the signer to false for the governance keypair since that gets
    // signed via CPI by the governance program.
    let instruction_accounts: Vec<AccountMeta> = instruction
        .accounts
        .clone()
        .into_iter()
        .map(|a| AccountMeta {
            pubkey: a.pubkey,
            is_signer: if a.pubkey == config.governance_id {
                false
            } else {
                a.is_signer
            },
            is_writable: a.is_writable,
        })
        .collect();

    let ix = execute_transaction(
        &GOVERNANCE_PROGRAM_ID,
        &config.governance_id,
        &proposal_id,
        &proposal_transaction_pubkey,
        &instruction_program_id,
        &instruction_accounts,
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


