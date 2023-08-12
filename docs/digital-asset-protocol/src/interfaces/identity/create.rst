src/interfaces/identity/create.rs
=================================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::collections::{BTreeMap};
use bebop::SliceWrapper;
use solana_program::account_info::AccountInfo;
use crate::api::{DigitalAssetProtocolError};
use crate::interfaces::ContextAction;
use crate::lifecycle::Lifecycle;
use crate::module::{DataItem, ModuleDataWrapper};
use crate::blob::Asset;
use crate::generated::schema::{ActionData, ModuleData, ModuleType, OwnershipModel};


pub struct Create<'info> {
    pub id: AccountInfo<'info>,
    pub owner: AccountInfo<'info>,
    pub payer: AccountInfo<'info>,
    pub uri: String,
}

impl<'info> Create<'info> {
    pub fn new(accounts: &[AccountInfo<'info>], action: ActionData) -> (Self, usize) {
        (
            Create {
                id: accounts[0].clone(),
                owner: accounts[1].clone(),
                payer: accounts[2].clone(),
                uri,
            },
            3
        )
    }
}

impl ContextAction for Create<'_> {
    fn lifecycle(&self) -> &Lifecycle {
        &Lifecycle::Create
    }

    fn run(&mut self) -> Result<(), DigitalAssetProtocolError> {
        let data = self.id.try_borrow_mut_data().map_err(|_| {
            DigitalAssetProtocolError::ActionError("Issue with Borrowing Data".to_string())
        })?;

        let modules = vec![
            ModuleType::Data,
            ModuleType::Signature,
            ModuleType::Ownership,
        ];
        let mut new_asset = Asset {
            layout: BTreeMap::new()
        };
        let owner_key = self.owner.key.to_bytes();
        for m in modules {
            let processor = ModuleType::to_processor(m);

            let data: Option<ModuleDataWrapper> = match m {
                ModuleType::Ownership => {
                    Some(ModuleDataWrapper::Structured(ModuleData::OwnershipData {
                        model: OwnershipModel::Single,
                        owner: SliceWrapper::from_raw(&owner_key)
                    }))
                }
                ModuleType::Data => {
                    let mut data = BTreeMap::new();
                    data.insert("uri".to_string(), DataItem::String(self.uri.clone()));
                    Some(ModuleDataWrapper::Unstructured(data))
                }
                _ => {
                    None
                }
            };
            processor.create(&mut new_asset, data)?;
        }
        Ok(())
    }
}

