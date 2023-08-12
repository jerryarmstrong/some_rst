src/processor/mod.rs
====================

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use std::{path::PathBuf, str::FromStr};

use anyhow::{anyhow, Result};
use borsh::BorshDeserialize;
use log::debug;
use solana_client::rpc_client::RpcClient;
use solana_program::{instruction::AccountMeta, pubkey::Pubkey};
use solana_sdk::signer::Signer;
use spl_associated_token_account::get_associated_token_address;
use spl_governance::{
    instruction::{
        add_signatory, cancel_proposal, cast_vote, create_proposal, deposit_governing_tokens,
        execute_transaction, insert_transaction, sign_off_proposal, withdraw_governing_tokens,
    },
    state::{
        governance::GovernanceV2,
        proposal::{get_proposal_address, ProposalV2},
        proposal_transaction::{get_proposal_transaction_address, ProposalTransactionV2},
        token_owner_record::{get_token_owner_record_address, TokenOwnerRecordV2},
        vote_record::Vote as SplVote,
    },
    state::{proposal::VoteType, realm::RealmV2},
};

use crate::{config, instruction::create_upgrade_program_instruction, Vote, GOVERNANCE_PROGRAM_ID};

mod cancel;
mod deposit;
mod execute;
mod get_gov_config;
mod update_config;
mod upgrade_program;
mod vote;
mod withdraw;

pub use cancel::*;
pub use deposit::*;
pub use execute::*;
pub use get_gov_config::*;
pub use update_config::*;
pub use upgrade_program::*;
pub use vote::*;
pub use withdraw::*;

#[derive(Clone, Debug, PartialEq, Eq)]
pub enum MintType {
    Member,
    Council,
}

impl FromStr for MintType {
    type Err = anyhow::Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s.to_lowercase().as_str() {
            "member" => Ok(MintType::Member),
            "council" => Ok(MintType::Council),
            _ => Err(anyhow!("Invalid mint type")),
        }
    }
}

fn get_realm_data(client: &RpcClient, realm: &Pubkey) -> Result<RealmV2> {
    let account = client.get_account(realm)?;
    let realm_data = RealmV2::deserialize(&mut account.data.as_slice())?;
    Ok(realm_data)
}

fn get_governance_data(client: &RpcClient, governance: &Pubkey) -> Result<GovernanceV2> {
    let account = client.get_account(governance)?;
    let governance_data = GovernanceV2::deserialize(&mut account.data.as_slice())?;
    Ok(governance_data)
}

fn get_governance_state<T>(client: &RpcClient, governance: &Pubkey) -> Result<T>
where
    T: borsh::BorshDeserialize,
{
    let account = client.get_account(governance)?;
    let governance_data = T::deserialize(&mut account.data.as_slice())?;
    Ok(governance_data)
}


