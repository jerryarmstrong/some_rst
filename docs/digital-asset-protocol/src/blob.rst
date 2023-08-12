src/blob.rs
===========

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::cell::{Ref, RefMut};
use std::collections::BTreeMap;
use crate::api::DigitalAssetProtocolError;
use bebop::{Record, SliceWrapper, SubRecord};
use solana_program::program_memory::sol_memset;
use solana_program::pubkey::Pubkey;
use crate::generated::schema::owned::{Blob, BlobContainer, DataItem, ModuleType, DataItemValue, ModuleData};

use crate::module::{ModuleDataWrapper, SchemaId};
use crate::required_field;

pub struct Asset {
    pub dirty: bool,
    layout: BTreeMap<ModuleType, ModuleDataWrapper>,
}


impl Asset {
    pub fn new() -> Asset {
        Asset {
            layout: BTreeMap::new(),
            dirty: true,
        }
    }

    pub fn set_module(&mut self, id: ModuleType, data: ModuleDataWrapper) {
        if !self.dirty {
            self.dirty = true;
        }
        self.layout.insert(id, data);
    }

    pub fn get_module(&mut self, id: ModuleType) -> Option<&mut ModuleDataWrapper> {
        self.layout.get_mut(&id)
    }

    pub fn save(mut self, destination: RefMut<&mut [u8]>) -> Result<(), DigitalAssetProtocolError> {
        let len = destination.len();
        let mut dest = destination;
        // Clear the data, this is the naive approach, we can optimize this with specific/tracked module offsets
        // todo pr to bebop to support @ offset serialization or intermediate buffer.
        // TODO -> at a higher level ensure account has enough space if not realloc.
        sol_memset(*dest, 0, len);
        let mut blobs = Vec::with_capacity(self.layout.len());
        for (id, data) in self.layout {
            let mut blob = Blob {
                module_id: Some(id as u8),
                structured_module: None,
                data_module: None,
            };
            match data {
                ModuleDataWrapper::Structured(md) => {
                    blob.structured_module = Some(md);
                }
                ModuleDataWrapper::Unstructured(data_module_data) => {
                    let mut uvec = Vec::with_capacity(data_module_data.len());
                    for (key, value) in data_module_data.into_iter() {
                        let di = DataItem {
                            key: key,
                            value: value
                        };
                        uvec.push(di);
                    }
                    blob.data_module = Some(uvec);
                }
            };
            blobs.push(blob);
        }
        let container = BlobContainer {
            blobs
        };
        container.serialize(&mut *dest)
            .map_err(|e| {
                DigitalAssetProtocolError::DeError(e.to_string())
            })?;
        Ok(())
    }

    fn load_layout(bc: BlobContainer) -> Result<BTreeMap<ModuleType, ModuleDataWrapper>, DigitalAssetProtocolError> {
        let mut layout = BTreeMap::new();
        for blob in bc.blobs {
            let module_id = blob.module_id;
            required_field!(module_id)?; //This macro might not be the best here
            let module_id = ModuleType::try_from(module_id.unwrap()).map_err(Into::into)?;
            match (blob.data_module, blob.structured_module) {
                (Some(data_items), None) => {
                    let mut bespoke_data = BTreeMap::new();
                    for di in data_items {

                        bespoke_data.insert(di.key.to_string(), di.value);
                    }
                    layout.insert(module_id, ModuleDataWrapper::Unstructured(bespoke_data));
                }
                (None, Some(module_data)) => {
                    layout.insert(module_id, ModuleDataWrapper::Structured(module_data));
                }
                _ => {
                    return Err(DigitalAssetProtocolError::DeError("Invalid Blob".to_string()));
                }
            }
        }
        Ok(layout)
    }

    pub fn load_mut(source: &mut [u8]) -> Result<Asset, DigitalAssetProtocolError> {
        let container = BlobContainer::deserialize(source).map_err(Into::into)?;

        Ok(Asset {
            dirty: false,
            layout: Asset::load_layout(container)?,
        })
    }

    pub fn load(source: &[u8]) -> Result<Asset, DigitalAssetProtocolError> {
        let container = BlobContainer::deserialize(source).map_err(Into::into)?;

        Ok(Asset {
            dirty: false,
            layout: Asset::load_layout(container)?,
        })
    }
}


