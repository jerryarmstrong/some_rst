trashheap/poc/supply.rs
=======================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use solana_program::pubkey::Pubkey;
use std::io::Result;
use crate::poc::{Action, Asset, Lifecycle, Modules, ModuleType, SolanaMock};

use borsh::{BorshSerialize, BorshDeserialize};

#[derive(BorshSerialize, BorshDeserialize)]
struct SupplyData {
    mint: Pubkey,
    max_supply: Option<u64>
}

#[derive(BorshSerialize, BorshDeserialize)]
struct Supply {
    data: SupplyData,
}

/// ROYALTIES ENFORCED AT PROTOCOL LEVEL like EIP 2981

impl ModuleType for Supply {
    fn id(&self) -> Modules {
        Modules::Supply
    }


    fn modify(&self, action: Action, asset: Asset) -> Result<Asset> {
        match action.lifecycle {
            Lifecycle::Update => {
                // TODO get old and new data from instruction
                Ok(asset)
            },
            Lifecycle::Burn => {
                //TODO -> Check transaction to see if money was exchanged
                Ok(asset)
            },
            Lifecycle::Delete => {
                //TODO -> Check transaction to see if money was exchanged
                Ok(asset)
            },
            Lifecycle::Create => {
                let max_supply: u64 = 10000000; ///get from context
                let mint_info = &action.context.accounts[0];


                Ok(asset)
            },
            _ => Ok(asset)
        }
    }
}


