accounts-db/src/tiered_storage/writer.rs
========================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! docs/src/proposals/append-vec-storage.md

use {
    crate::{
        account_storage::meta::{StorableAccountsWithHashesAndWriteVersions, StoredAccountInfo},
        storable_accounts::StorableAccounts,
        tiered_storage::{
            error::TieredStorageError, file::TieredStorageFile, footer::TieredStorageFooter,
            TieredStorageFormat, TieredStorageResult,
        },
    },
    solana_sdk::{account::ReadableAccount, hash::Hash},
    std::{borrow::Borrow, path::Path},
};

#[derive(Debug)]
pub struct TieredStorageWriter<'format> {
    storage: TieredStorageFile,
    format: &'format TieredStorageFormat,
}

impl<'format> TieredStorageWriter<'format> {
    pub fn new(
        file_path: impl AsRef<Path>,
        format: &'format TieredStorageFormat,
    ) -> TieredStorageResult<Self> {
        Ok(Self {
            storage: TieredStorageFile::new_writable(file_path)?,
            format,
        })
    }

    pub fn write_accounts<
        'a,
        'b,
        T: ReadableAccount + Sync,
        U: StorableAccounts<'a, T>,
        V: Borrow<Hash>,
    >(
        &self,
        _accounts: &StorableAccountsWithHashesAndWriteVersions<'a, 'b, T, U, V>,
        _skip: usize,
    ) -> TieredStorageResult<Vec<StoredAccountInfo>> {
        let footer = TieredStorageFooter {
            account_meta_format: self.format.account_meta_format,
            owners_block_format: self.format.owners_block_format,
            account_block_format: self.format.account_block_format,
            account_index_format: self.format.account_index_format,
            ..TieredStorageFooter::default()
        };

        footer.write_footer_block(&self.storage)?;

        Err(TieredStorageError::Unsupported())
    }
}


