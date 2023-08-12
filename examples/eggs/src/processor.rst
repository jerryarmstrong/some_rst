examples/eggs/src/processor.rs
==============================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    //! Program state processor

use crate::{
    instruction::EggsInstruction,
    state::{Egg, InitEggParams},
    utils::*,
};
use borsh::BorshDeserialize;
use randomness_oracle_program::read_value;
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint::ProgramResult,
    msg,
    program_pack::Pack,
    pubkey::Pubkey,
    rent::Rent,
    sysvar::Sysvar,
};

/// Program state handler.
pub struct Processor {}
impl Processor {
    /// Process CreateEgg instruction
    pub fn create_egg(program_id: &Pubkey, accounts: &[AccountInfo]) -> ProgramResult {
        let account_info_iter = &mut accounts.iter();
        let egg_info = next_account_info(account_info_iter)?;
        let randomness_oracle_info = next_account_info(account_info_iter)?;
        let rent_info = next_account_info(account_info_iter)?;
        let rent = &Rent::from_account_info(rent_info)?;

        assert_rent_exempt(rent, egg_info)?;
        assert_owned_by(egg_info, program_id)?;

        // Get egg state
        let mut egg = Egg::unpack_unchecked(&egg_info.data.borrow())?;
        assert_uninitialized(&egg)?;

        let (gen, _) = read_value(randomness_oracle_info)?;

        egg.init(InitEggParams { gen });

        Egg::pack(egg, *egg_info.data.borrow_mut())?;

        Ok(())
    }

    /// Instruction processing router
    pub fn process_instruction(
        program_id: &Pubkey,
        accounts: &[AccountInfo],
        input: &[u8],
    ) -> ProgramResult {
        let instruction = EggsInstruction::try_from_slice(input)?;

        match instruction {
            EggsInstruction::CreateEgg => {
                msg!("EggsInstruction: CreateEgg");
                Self::create_egg(program_id, accounts)
            }
        }
    }
}


