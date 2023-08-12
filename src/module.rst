src/module.rs
=============

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use std::cmp::Ordering;
use std::collections::BTreeMap;
use bebop::Record;
use solana_program::account_info::AccountInfo;
use crate::api::DigitalAssetProtocolError;
use crate::blob::Asset;
use crate::generated::schema::owned::{ModuleType, ModuleData, DataItemValue};
use crate::lifecycle::Lifecycle;
use crate::modules::OWNERSHIP_MODULE_PROCESSOR;

pub trait Module {
    fn act<A, D>(&self, context: Lifecycle, asset: &mut Asset) -> Asset;
}

pub enum ModuleDataWrapper {
    Structured(ModuleData),
    Unstructured(BTreeMap<String, DataItemValue>),
}

pub type SchemaId = [u8; 16];

pub trait ModuleProcessor {
    fn create<'raw>(&self, asset: &mut Asset)
                    -> Result<(), DigitalAssetProtocolError>;
}

pub struct NullModuleProcessor {}

pub static NULL_MODULE_PROCESSOR: NullModuleProcessor = NullModuleProcessor {};

pub struct AccountMap<'raw> {
    map: BTreeMap<String, &'raw AccountInfo<'raw>>,
}

impl<'raw> AccountMap<'raw> {
    pub fn insert(&mut self, key: String, info: &'raw AccountInfo<'raw>) {
        self.map.insert(key, info);
    }

    pub fn get(&self, key: String) -> Result<&'raw AccountInfo, DigitalAssetProtocolError> {
        self.map.get(&key).map(|a| *a).ok_or(DigitalAssetProtocolError::InterfaceNoImpl)
    }
}

impl ModuleProcessor for NullModuleProcessor {
    fn create<'raw>(&self, asset: &mut Asset)
                    -> Result<(), DigitalAssetProtocolError> {
        Ok(())
    }
}

impl ModuleType {
    pub fn to_data(module: ModuleType, raw_data: &[u8]) -> Result<Option<ModuleData>, DigitalAssetProtocolError> {
        ModuleData::deserialize(raw_data)
            .map_err(|e| e.into())
            .and_then(|data| {
                match (module, &data) {
                    (ModuleType::Ownership, &ModuleData::OwnershipData { .. }) => Ok(Some(data)),
                    _ => Err(DigitalAssetProtocolError::ModuleError("Module Datatype mismatch".to_string()))
                }
            })
    }

    pub fn to_processor(module: ModuleType) -> &'static dyn ModuleProcessor {
        match module {
            ModuleType::Ownership => &OWNERSHIP_MODULE_PROCESSOR,
            _ => &NULL_MODULE_PROCESSOR
        }
    }
}

#[derive(Ord, PartialOrd, Eq, PartialEq)]
pub enum ModuleId {
    Module(ModuleType),
    Extension(SchemaId),
}

impl PartialOrd<Self> for ModuleType {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        let d: u8 = u8::from(*self);
        let o: u8 = u8::from(*other);
        d.partial_cmp(&o)
    }
}

impl Ord for ModuleType {
    fn cmp(&self, other: &Self) -> Ordering {
        let d: u8 = u8::from(*self);
        let o: u8 = u8::from(*other);
        d.cmp(&o)
    }
}

