trashheap/poc/ownership.rs
==========================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::io::{Error, ErrorKind};
use solana_program::pubkey::Pubkey;
use crate::poc::{Action, Asset, Lifecycle, Modules, ModuleType, SolanaMock};
use std::io::Result;
use borsh::{BorshSerialize, BorshDeserialize};

#[derive(Debug, Clone, BorshSerialize, BorshDeserialize, Eq, PartialEq)]
pub enum  OwnershipModel {
    Address,
    Fanout,
}

#[derive(Debug, Clone, BorshSerialize, BorshDeserialize, Eq, PartialEq)]
pub struct OwnershipData {
    pub ownership_model: OwnershipModel,
    // A wallet or a shared ownership mechanism such as a fanout
    pub owner: Pubkey
}

#[derive(Debug, Clone, BorshSerialize, BorshDeserialize, Eq, PartialEq)]
pub struct Ownership {
    pub data: OwnershipData,
}

/// ROYALTIES ENFORCED AT PROTOCOL LEVEL like EIP 2981

impl ModuleType for Ownership {
    fn id(&self) -> Modules {
        Modules::Ownership
    }


    fn modify(&self, action: Action, asset: Asset) -> Result<Asset> {
        match action.lifecycle {
            Lifecycle::Create => {
                let data = OwnershipModeldeserialize(action.context.data).map_err(|e| {Error::new(ErrorKind::InvalidData, e)})?;
                let owner = action.context.accounts[0];
                Ok(asset)
            }
            Lifecycle::Update => {
                // Update Ownership
                Ok(asset)
            }
            _ => Ok(asset)
        }
    }
}


