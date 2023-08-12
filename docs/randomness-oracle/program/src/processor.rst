program/src/processor.rs
========================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    //! Program state processor.

use crate::{
    instruction::RandomnessOracleInstruction,
    state::{InitRandomnessOracleParams, RandomnessOracle},
    utils::*,
};
use borsh::BorshDeserialize;
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    program_pack::Pack,
    pubkey::Pubkey,
    sysvar::Sysvar,
};

/// Program state handler.
pub struct Processor {}
impl Processor {
    /// Process `InitRandomnessOracle` instruction.
    pub fn init_randomness_oracle(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
        let account_info_iter = &mut accounts.iter();
        let randomness_oracle_info = next_account_info(account_info_iter)?;
        let authority_info = next_account_info(account_info_iter)?;
        let clock_info = next_account_info(account_info_iter)?;
        let clock = solana_program::clock::Clock::from_account_info(clock_info)?;

        // Check signer
        assert_signer(authority_info)?;

        // Check random oracle owner
        assert_owned_by(randomness_oracle_info, program_id)?;

        // Get state
        let mut randomness_oracle =
            RandomnessOracle::unpack_unchecked(&randomness_oracle_info.data.borrow())?;

        // Initialize
        randomness_oracle.init(InitRandomnessOracleParams {
            authority: *authority_info.key,
            slot: clock.slot,
        });

        // Save state
        RandomnessOracle::pack(randomness_oracle, *randomness_oracle_info.data.borrow_mut())?;

        Ok(())
    }

    /// Process `UpdateRandomnessOracle` instruction.
    pub fn update_randomness_oracle(
        program_id: &Pubkey,
        accounts: &[AccountInfo],
        value: [u8; 32],
    ) -> ProgramResult {
        let account_info_iter = &mut accounts.iter();
        let randomness_oracle_info = next_account_info(account_info_iter)?;
        let authority_info = next_account_info(account_info_iter)?;
        let clock_info = next_account_info(account_info_iter)?;
        let clock = solana_program::clock::Clock::from_account_info(clock_info)?;

        // Check signer
        assert_signer(authority_info)?;

        // Check random oracle owner
        assert_owned_by(randomness_oracle_info, program_id)?;

        // Get state
        let mut randomness_oracle =
            RandomnessOracle::unpack(&randomness_oracle_info.data.borrow())?;

        // Check random oracle authority
        if randomness_oracle.authority != *authority_info.key {
            return Err(ProgramError::InvalidArgument);
        }

        // Update
        randomness_oracle.update(value, clock.slot);

        // Save state
        RandomnessOracle::pack(randomness_oracle, *randomness_oracle_info.data.borrow_mut())?;

        Ok(())
    }

    /// Instruction processing router.
    pub fn process_instruction(
        program_id: &Pubkey,
        accounts: &[AccountInfo],
        input: &[u8],
    ) -> ProgramResult {
        let instruction = RandomnessOracleInstruction::try_from_slice(input)?;

        match instruction {
            RandomnessOracleInstruction::InitRandomnessOracle => {
                msg!("RandomnessOracleInstruction: InitRandomnessOracle");
                Self::init_randomness_oracle(program_id, accounts)
            }
            RandomnessOracleInstruction::UpdateRandomnessOracle { value } => {
                msg!("RandomnessOracleInstruction: UpdateRandomnessOracle");
                Self::update_randomness_oracle(program_id, accounts, value)
            }
        }
    }
}


