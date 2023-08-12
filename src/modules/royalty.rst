src/modules/royalty.rs
======================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::io::BufWriter;
use bebop::{Record, SliceWrapper, SubRecord};
use lazy_static::lazy_static;
use solana_program::account_info::AccountInfo;
use crate::api::DigitalAssetProtocolError;
use crate::blob::{Asset, Blob};
use crate::generated::schema::{ModuleType};
use crate::module::{ModuleDataWrapper, ModuleId, ModuleProcessor};


pub struct OwnershipModuleProcessor {}

pub static OWNERSHIP_MODULE_PROCESSOR: OwnershipModuleProcessor = OwnershipModuleProcessor {};

impl ModuleProcessor for OwnershipModuleProcessor {
    fn create<'raw>(&self,
                    asset: &mut Asset<'raw>,
                    module_data: Option<ModuleDataWrapper<'raw>>,
    )
                    -> Result<(), DigitalAssetProtocolError> {
        let ownership_data = match module_data {
            Some(ModuleDataWrapper::Structured(d)) => Ok(d),
            _ => {
                Err(DigitalAssetProtocolError::ModuleError("Incorrect Data Type for Module".to_string()))
            }
        }?;

        let mut raw_data = Vec::with_capacity(ownership_data.serialized_size());
        ownership_data.serialize(&mut raw_data)
            .map_err(|e| {
                DigitalAssetProtocolError::ModuleError(e.to_string())
            })?;
        let blob = Blob {
            schema: ModuleId::Module(ModuleType::Ownership),
            data: raw_data,
            _runtime_data: Some(ownership_data.to_owned()),
        };
        asset.layout.insert(ModuleId::Module(ModuleType::Ownership), blob);
        Ok(())
    }
}

