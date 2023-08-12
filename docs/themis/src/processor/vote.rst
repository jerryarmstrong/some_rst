src/processor/vote.rs
=====================

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use super::*;

pub struct VoteArgs {
    pub keypair_path: Option<PathBuf>,
    pub rpc_url: Option<String>,
    pub proposal_id: Option<Pubkey>,
    pub latest: bool,
    pub mint_type: MintType,
    pub vote_choice: Vote,
}

pub fn vote(args: VoteArgs) -> Result<()> {
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

    let token_owner_record: TokenOwnerRecordV2 =
        get_governance_state(&config.client, &proposal.token_owner_record)?;

    let proposal_owner_record = get_token_owner_record_address(
        &GOVERNANCE_PROGRAM_ID,
        &config.realm_id,
        &governing_token_mint,
        &token_owner_record.governing_token_owner,
    );

    debug!("Proposal Owner Record: {proposal_owner_record}");

    let voter_token_owner_record = get_token_owner_record_address(
        &GOVERNANCE_PROGRAM_ID,
        &config.realm_id,
        &governing_token_mint,
        &config.keypair.pubkey(),
    );

    debug!("Voter Token Owner Record: {voter_token_owner_record}");

    let vote: SplVote = args.vote_choice.into();

    let ix = cast_vote(
        &GOVERNANCE_PROGRAM_ID,
        &config.realm_id,
        &config.governance_id,
        &proposal_id,
        &proposal_owner_record,
        &voter_token_owner_record,
        &config.keypair.pubkey(),
        &governing_token_mint,
        &config.keypair.pubkey(),
        None,
        None,
        vote,
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


