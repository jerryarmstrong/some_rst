src/modules/signature.rs
========================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use solana_program::account_info::AccountInfo;
use crate::api::DigitalAssetProtocolError;
use crate::blob::Asset;
use crate::module::{ModuleProcessor, ModuleDataWrapper};

pub struct SignatureModuleProcessor {}

pub static SIGNATURE_MODULE_PROCESSOR: SignatureModuleProcessor = SignatureModuleProcessor {};

impl ModuleProcessor for SignatureModuleProcessor {
    fn create(&self,
                    asset: &mut Asset
    )
                    -> Result<(), DigitalAssetProtocolError> {
        Ok(())
    }
}

