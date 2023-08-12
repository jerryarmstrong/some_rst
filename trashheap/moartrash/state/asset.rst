trashheap/moartrash/state/asset.rs
==================================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::borrow::BorrowMut;
use crate::state::blob::{Blob, Blobbed, BlobBorsh, BlobId};
use std::collections::{BTreeMap, BTreeSet};
use std::io::Write;
use borsh::{BorshDeserialize, BorshSerialize};
use solana_program::msg;
use solana_program::program_error::ProgramError;
use crate::modules::{Module};
use thiserror::Error;
use crate::state::asset::AssetError::InvalidAsset;
use crate::state::blob;

#[derive(Error, Debug)]
pub enum AssetError {
    #[error("Instruction Error: Invalid {0}")]
    InstructionError(String),
    #[error("Invalid Lifecycle: {0} does not exist")]
    InvalidLifeCycle(String),
    #[error("BorshDeserialize failed {0}")]
    InvalidAsset(String),
}

pub struct Asset<'a> {
    data: BTreeMap<BlobId, Vec<u8>>,
    runtime: RuntimeAsset<'a>
}

impl Asset<'_> {
    pub fn modules(&self) -> BTreeSet<&Module> {
        self.data.keys().map(|ik|{
            match ik {
                BlobId::Module(m) => m,
                _ => &Module::Extension
            }
        }).collect()
    }

    pub fn deserialize(buf: &mut &[u8]) -> std::io::Result<Self> {
        let b : BTreeMap<BlobId, Vec<u8>> = BorshDeserialize::deserialize(buf)?;
        Ok(Asset{
            data: b,
            runtime: RuntimeAsset::default()
        })
    }

    pub fn serialize<T: 'static +  BorshSerialize + BorshDeserialize, W: Write>(&mut self, writer: &mut W) -> std::io::Result<()> {
        for (id, blob) in self.runtime.data.iter_mut() {
            if blob.dirty() {
                self.data.entry(id.to_owned()).and_modify(move |ve| {
                    let blob_c = Blob::<T>::blob::<T>(blob).unwrap();
                    // TODO -> Dont fail silently
                    Blob::serialize(blob_c, ve)
                        .map_err(|_| {
                            msg!("Serialization Err in Blob {:?}", id)
                        })
                        .unwrap_or(())
                });
            }
        }
        Ok(())
    }
}



#[derive(Default)]
pub struct RuntimeAsset<'a> {
    data: BTreeMap<BlobId, &'a dyn Blobbed>,
}


impl Asset<'_> {

    pub fn try_deserialize<'a>(bytes: &mut &[u8]) -> Result<Asset<'a>, AssetError> {
        // We need to have some sort of size limit
        Asset::deserialize(bytes).map_err(|e| InvalidAsset(e.to_string()).into())
    }

    pub fn get_raw_module_data(&mut self, module: Module) -> Option<&mut Vec<u8>> {
        self.data.get_mut(&BlobId::Module(module))
    }

    // pub fn get_module_data<T: BorshDeserialize + BorshSerialize>(&mut self, module: Module) -> Option<&mut Blob<T>> {
    //     let entry = self.get_raw_module_data(module);
    //     entry.and_then(|e| {
    //         Blob::<T>::deserialize(e.as_mut_slice(), BlobId::Module(module)).as_mut().ok()
    //     })
    // }

    pub fn set_module_data<T, F>(&mut self, module: Module, modifier: F)
        where
            T: BorshDeserialize + BorshSerialize,
            F: FnOnce(&mut &dyn Blobbed) -> ()
    {
        self.runtime.data.entry(BlobId::Module(module)).and_modify(modifier);
    }
}


