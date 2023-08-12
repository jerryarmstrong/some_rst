trashheap/poc/governed.rs
=========================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::io::{Error, ErrorKind};
use solana_program::pubkey::Pubkey;
use crate::poc::{Action, Asset, Lifecycle, Modules, ModuleType, SolanaMock};
use std::io::Result;


struct Authority {
    address: Pubkey,
    scopes: Vec<Modules>
}

struct GovernedData {
    authorities: Vec<Authority>
}

struct Governed {
    data: GovernedData,
}

/// ROYALTIES ENFORCED AT PROTOCOL LEVEL like EIP 2981

impl ModuleType for Governed {
    fn id(&self) -> Modules {
        Modules::Governed
    }


    fn modify(&self, action: Action, asset: Asset) -> Result<Asset> {





        Asset {
            standard: NFT,
            layout: Map{
                Ownership: OwnershipModule{
                    ownership_model: Single,
                    owner: Pubkey::new(),
                },
                Royalty: {
                    sale_royalty_percent: 3, //% of sale price
                    counter: 0, // Number of Sales
                    locked: false, //Royalties are volotile
                    /// multi target support or 1st class support for groups(hydra)
                    royalty_target: RoyaltyTarget::Creators
                },
                }
            }




        match action.lifecycle {
            Lifecycle::Create => {
                // Set Update
                Ok(asset)
            },
            Lifecycle::Update => {

                Ok(asset)
            },

            _ => Ok(asset)
        }
    }
}


