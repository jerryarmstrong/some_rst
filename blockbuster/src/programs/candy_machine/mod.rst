blockbuster/src/programs/candy_machine/mod.rs
=============================================

Last edited: 2023-06-27 20:46:29

Contents:

.. code-block:: rs

    use crate::{
    error::BlockbusterError,
    program_handler::{ParseResult, ProgramParser},
    programs::{
        candy_machine::state::{CandyMachine, CollectionPDA, FreezePDA},
        ProgramParseResult,
    },
};
use plerkle_serialization::AccountInfo;
use solana_sdk::{borsh::try_from_slice_unchecked, pubkey::Pubkey, pubkeys};
use std::convert::TryInto;

pub mod state;

pubkeys!(
    candy_machine_id,
    "cndy3Z4yapfJBmL3ShUp5exZKqR3z33thTzeNMm2gRZ"
);

// Anchor account discriminators.
pub const CANDY_MACHINE_DISCRIMINATOR: [u8; 8] = [51, 173, 177, 113, 25, 241, 109, 189];
pub const COLLECTION_PDA_DISCRIMINATOR: [u8; 8] = [203, 128, 119, 125, 234, 89, 232, 157];
pub const FREEZE_PDA_DISCRIMINATOR: [u8; 8] = [154, 58, 148, 24, 101, 200, 243, 127];

#[allow(clippy::large_enum_variant)]
pub enum CandyMachineAccountData {
    CandyMachine(CandyMachine),
    CollectionPDA(CollectionPDA),
    FreezePDA(FreezePDA),
}

impl ParseResult for CandyMachineAccountData {
    fn result(&self) -> &Self
    where
        Self: Sized,
    {
        self
    }
    fn result_type(&self) -> ProgramParseResult {
        ProgramParseResult::CandyMachine(self)
    }
}

pub struct CandyMachineParser;

impl ProgramParser for CandyMachineParser {
    fn key(&self) -> Pubkey {
        candy_machine_id()
    }

    fn key_match(&self, key: &Pubkey) -> bool {
        key == &candy_machine_id()
    }
    fn handles_account_updates(&self) -> bool {
        true
    }

    fn handles_instructions(&self) -> bool {
        false
    }
    fn handle_account(
        &self,
        account_info: &AccountInfo,
    ) -> Result<Box<dyn ParseResult + 'static>, BlockbusterError> {
        let account_data = if let Some(account_info) = account_info.data() {
            account_info.iter().collect::<Vec<_>>()
        } else {
            return Err(BlockbusterError::DeserializationError);
        };

        let discriminator: [u8; 8] = account_data[0..8].try_into().unwrap();

        let account_type = match discriminator {
            CANDY_MACHINE_DISCRIMINATOR => {
                let candy_machine = try_from_slice_unchecked(&account_data[8..])?;
                CandyMachineAccountData::CandyMachine(candy_machine)
            }
            COLLECTION_PDA_DISCRIMINATOR => {
                let collection_pda = try_from_slice_unchecked(&account_data[8..])?;
                CandyMachineAccountData::CollectionPDA(collection_pda)
            }
            FREEZE_PDA_DISCRIMINATOR => {
                let freeze_pda = try_from_slice_unchecked(&account_data[8..])?;
                CandyMachineAccountData::FreezePDA(freeze_pda)
            }
            _ => return Err(BlockbusterError::UnknownAccountDiscriminator),
        };

        Ok(Box::new(account_type))
    }
}


