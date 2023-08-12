trashheap/poc/creators.rs
=========================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::io::{Error, ErrorKind};
use solana_program::pubkey::Pubkey;
use crate::poc::{Action, Asset, Lifecycle, Modules, ModuleType, SolanaMock};
use std::io::Result;
use borsh::{BorshSerialize, BorshDeserialize};

#[derive(Debug, Clone, BorshSerialize, BorshDeserialize, Copy, Default, Eq, PartialEq)]
pub struct Creator {
    pub address: Pubkey,
    pub share: u8,
    pub verified: bool,
}

#[derive(Debug, Clone, BorshSerialize, BorshDeserialize, Eq, PartialEq)]
pub struct CreatorsData {
    pub creators: Vec<Creator>,
}

#[derive(Debug, Clone, BorshSerialize, BorshDeserialize, Eq, PartialEq)]
pub struct Creators {
    pub data: CreatorsData,
}

/// ROYALTIES ENFORCED AT PROTOCOL LEVEL like EIP 2981

impl ModuleType for Creators {
    fn id(&self) -> Modules {
        Modules::Creators
    }


    fn modify(&self, action: Action, asset: Asset) -> Result<Asset> {
        match action.lifecycle {
            Lifecycle::Create => {
                // Set Creators
                Ok(asset)
            }
            Lifecycle::Update => {
                // Update Creators
                Ok(asset)
            }

            _ => Ok(asset)
        }
    }
}


