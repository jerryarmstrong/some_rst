program/src/processor/migrate/mod.rs
====================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: rs

    mod processor;
mod validate;

pub use processor::*;
use spl_token::state::{Account, Mint};
use validate::*;

use super::*;

pub(crate) struct AccountContext<'a> {
    pub(crate) program_id: &'a Pubkey,
    pub(crate) payer_info: &'a AccountInfo<'a>,
    pub(crate) metadata_info: &'a AccountInfo<'a>,
    pub(crate) edition_info: &'a AccountInfo<'a>,
    pub(crate) mint_info: &'a AccountInfo<'a>,
    pub(crate) token_owner_info: &'a AccountInfo<'a>,
    pub(crate) token_owner_program_info: &'a AccountInfo<'a>,
    pub(crate) token_owner_program_buffer_info: &'a AccountInfo<'a>,
    pub(crate) delegate_record_info: &'a AccountInfo<'a>,
    pub(crate) migration_state_info: &'a AccountInfo<'a>,
    pub(crate) program_signer_info: &'a AccountInfo<'a>,
    pub(crate) auth_rule_set_info: &'a AccountInfo<'a>,
    pub(crate) system_program_info: &'a AccountInfo<'a>,
    pub(crate) sysvar_instructions_info: &'a AccountInfo<'a>,
    pub(crate) token_metadata_program_info: &'a AccountInfo<'a>,
    pub(crate) spl_token_program_info: &'a AccountInfo<'a>,
}

pub(crate) struct DataContext<'a> {
    pub(crate) metadata: &'a Metadata,
    pub(crate) collection_metadata: &'a Metadata,
    pub(crate) migration_state: &'a MigrationState,
    pub(crate) mint: &'a Mint,
    pub(crate) token: &'a Account,
}


