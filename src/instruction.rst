src/instruction.rs
==================

Last edited: 2023-07-17 22:54:02

Contents:

.. code-block:: rs

    use std::env;
use std::str::FromStr;

use anyhow::{anyhow, Result};
use borsh::BorshSerialize;
use solana_program::pubkey::Pubkey;
use solana_program::sysvar::{clock::ID as sysvar_clock, rent::ID as rent_sysvar};
use spl_governance::instruction::GovernanceInstruction;
use spl_governance::state::governance::GovernanceConfig;
use spl_governance::state::proposal_transaction::{AccountMetaData, InstructionData};

use crate::{BPF_UPLOADER_ID, GOVERNANCE_PROGRAM_ID};

pub fn create_upgrade_program_instruction(
    source_buffer: Pubkey,
    spill_account: Pubkey,
    upgrade_authority: Pubkey,
) -> Result<InstructionData> {
    let program_data = Pubkey::from_str(
        &env::var("PROGRAM_DATA").map_err(|_| anyhow!("Missing PROGRAM_DATA env var."))?,
    )?;
    let program_id = Pubkey::from_str(
        &env::var("PROGRAM_ID").map_err(|_| anyhow!("Missing PROGRAM_ID env var."))?,
    )?;

    Ok(InstructionData {
        program_id: BPF_UPLOADER_ID,
        accounts: vec![
            AccountMetaData {
                pubkey: program_data,
                is_signer: false,
                is_writable: true,
            },
            AccountMetaData {
                pubkey: program_id,
                is_signer: false,
                is_writable: true,
            },
            AccountMetaData {
                pubkey: source_buffer,
                is_signer: false,
                is_writable: true,
            },
            AccountMetaData {
                pubkey: spill_account,
                is_signer: false,
                is_writable: true,
            },
            AccountMetaData {
                pubkey: rent_sysvar,
                is_signer: false,
                is_writable: false,
            },
            AccountMetaData {
                pubkey: sysvar_clock,
                is_signer: false,
                is_writable: false,
            },
            AccountMetaData {
                pubkey: upgrade_authority,
                is_signer: true,
                is_writable: true,
            },
        ],
        data: vec![3, 0, 0, 0],
    })
}

pub fn create_set_governance_config_instruction(
    config: GovernanceConfig,
) -> Result<InstructionData> {
    let governance_id = Pubkey::from_str(
        &env::var("GOVERNANCE_ID").map_err(|_| anyhow!("Missing GOVERNANCE_ID env var."))?,
    )?;

    let instruction = GovernanceInstruction::SetGovernanceConfig { config };

    Ok(InstructionData {
        program_id: GOVERNANCE_PROGRAM_ID,
        accounts: vec![AccountMetaData {
            pubkey: governance_id,
            is_signer: true,
            is_writable: true,
        }],
        data: instruction.try_to_vec()?,
    })
}


