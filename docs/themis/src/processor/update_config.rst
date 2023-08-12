src/processor/update_config.rs
==============================

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use chrono::Utc;
use spl_governance::state::enums::VoteThresholdPercentage;

use crate::instruction::create_set_governance_config_instruction;

use super::*;

pub struct UpdateConfigArgs {
    pub keypair_path: Option<PathBuf>,
    pub rpc_url: Option<String>,
    pub mint_type: MintType,
    pub vote_threshold_percentage: Option<u8>,
    pub min_council_weight_to_create_proposal: Option<u64>,
    pub min_transaction_hold_up_time: Option<u32>,
    pub max_voting_time: Option<u32>,
    pub proposal_cool_off_time: Option<u32>,
    pub min_comunity_weight_to_create_proposal: Option<u64>,
}

pub fn update_config(args: UpdateConfigArgs) -> Result<()> {
    let config = config::CliConfig::new(args.keypair_path, args.rpc_url)?;

    let realm = get_realm_data(&config.client, &config.realm_id)?;
    let governance = get_governance_data(&config.client, &config.governance_id)?;
    let mut governance_config = governance.config;

    let dt = Utc::now();
    let name = format!(
        "Update governance config {}",
        dt.format("%Y-%m-%d %H:%M:%S")
    );
    let description = format!("Update governance {} config", config.governance_id);
    let options = vec!["Approve".to_string()];

    debug!("Current Governance Config: {:#?}", governance_config);

    let governing_token_mint = match args.mint_type {
        MintType::Member => realm.community_mint,
        MintType::Council => realm
            .config
            .council_mint
            .ok_or_else(|| anyhow!("Council mint not found"))?,
    };

    let proposal_index: u32 = governance.proposals_count;

    let proposal_owner_record = get_token_owner_record_address(
        &GOVERNANCE_PROGRAM_ID,
        &config.realm_id,
        &governing_token_mint,
        &config.keypair.pubkey(),
    );

    let create_ix = create_proposal(
        &GOVERNANCE_PROGRAM_ID,
        &config.governance_id,
        &proposal_owner_record,
        &config.keypair.pubkey(),
        &config.keypair.pubkey(),
        None,
        &config.realm_id,
        name,
        description,
        &governing_token_mint,
        VoteType::SingleChoice,
        options,
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

    // Get config values
    if let Some(vote_threshold_percentage) = args.vote_threshold_percentage {
        governance_config.vote_threshold_percentage =
            VoteThresholdPercentage::YesVote(vote_threshold_percentage);
    }
    if let Some(min_council_weight_to_create_proposal) = args.min_council_weight_to_create_proposal
    {
        governance_config.min_council_weight_to_create_proposal =
            min_council_weight_to_create_proposal;
    }
    if let Some(min_transaction_hold_up_time) = args.min_transaction_hold_up_time {
        governance_config.min_transaction_hold_up_time = min_transaction_hold_up_time;
    }
    if let Some(max_voting_time) = args.max_voting_time {
        governance_config.max_voting_time = max_voting_time;
    }
    if let Some(proposal_cool_off_time) = args.proposal_cool_off_time {
        governance_config.proposal_cool_off_time = proposal_cool_off_time;
    }
    if let Some(min_comunity_weight_to_create_proposal) =
        args.min_comunity_weight_to_create_proposal
    {
        governance_config.min_community_weight_to_create_proposal =
            min_comunity_weight_to_create_proposal;
    }

    debug!("New Governance Config: {:#?}", governance_config);
    let upgrade_config_ix = create_set_governance_config_instruction(governance_config)?;

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
        vec![upgrade_config_ix],
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


