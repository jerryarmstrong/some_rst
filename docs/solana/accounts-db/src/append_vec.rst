accounts-db/src/append_vec.rs
=============================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! Persistent storage for accounts.
//!
//! For more information, see:
//!
//! <https://docs.solana.com/implemented-proposals/persistent-account-storage>

use {
    crate::{
        account_storage::meta::{
            AccountMeta, StorableAccountsWithHashesAndWriteVersions, StoredAccountInfo,
            StoredAccountMeta, StoredMeta, StoredMetaWriteVersion,
        },
        accounts_file::{AccountsFileError, Result, ALIGN_BOUNDARY_OFFSET},
        storable_accounts::StorableAccounts,
        u64_align,
    },
    log::*,
    memmap2::MmapMut,
    solana_sdk::{
        account::{AccountSharedData, ReadableAccount},
        clock::Slot,
        hash::Hash,
        pubkey::Pubkey,
        stake_history::Epoch,
    },
    std::{
        borrow::Borrow,
        convert::TryFrom,
        fs::{remove_file, OpenOptions},
        io::{Seek, SeekFrom, Write},
        mem,
        path::{Path, PathBuf},
        sync::{
            atomic::{AtomicU64, AtomicUsize, Ordering},
            Mutex,
        },
    },
    thiserror::Error,
};

pub mod test_utils;

/// size of the fixed sized fields in an append vec
/// we need to add data len and align it to get the actual stored size
pub const STORE_META_OVERHEAD: usize = 136;

/// Returns the size this item will take to store plus possible alignment padding bytes before the next entry.
/// fixed-size portion of per-account data written
/// plus 'data_len', aligned to next boundary
pub fn aligned_stored_size(data_len: usize) -> usize {
    u64_align!(STORE_META_OVERHEAD + data_len)
}

pub const MAXIMUM_APPEND_VEC_FILE_SIZE: u64 = 16 * 1024 * 1024 * 1024; // 16 GiB

#[derive(Error, Debug)]
/// An enum for AppendVec related errors.
pub enum AppendVecError {
    #[error("too small file size {0} for AppendVec")]
    FileSizeTooSmall(usize),

    #[error("too large file size {0} for AppendVec")]
    FileSizeTooLarge(usize),

    #[error("incorrect layout/length/data in the appendvec at path {}", .0.display())]
    IncorrectLayout(PathBuf),

    #[error("offset ({0}) is larger than file size ({1})")]
    OffsetOutOfBounds(usize, usize),
}

pub struct AppendVecAccountsIter<'append_vec> {
    append_vec: &'append_vec AppendVec,
    offset: usize,
}

impl<'append_vec> AppendVecAccountsIter<'append_vec> {
    pub fn new(append_vec: &'append_vec AppendVec) -> Self {
        Self {
            append_vec,
            offset: 0,
        }
    }
}

impl<'append_vec> Iterator for AppendVecAccountsIter<'append_vec> {
    type Item = StoredAccountMeta<'append_vec>;

    fn next(&mut self) -> Option<Self::Item> {
        if let Some((account, next_offset)) = self.append_vec.get_account(self.offset) {
            self.offset = next_offset;
            Some(account)
        } else {
            None
        }
    }
}

#[derive(Error, Debug, PartialEq, Eq)]
pub enum MatchAccountOwnerError {
    #[error("The account owner does not match with the provided list")]
    NoMatch,
    #[error("Unable to load the account")]
    UnableToLoad,
}

/// References to account data stored elsewhere. Getting an `Account` requires cloning
/// (see `StoredAccountMeta::clone_account()`).
#[derive(PartialEq, Eq, Debug)]
pub struct AppendVecStoredAccountMeta<'append_vec> {
    pub meta: &'append_vec StoredMeta,
    /// account data
    pub account_meta: &'append_vec AccountMeta,
    pub(crate) data: &'append_vec [u8],
    pub(crate) offset: usize,
    pub(crate) stored_size: usize,
    pub(crate) hash: &'append_vec Hash,
}

impl<'append_vec> AppendVecStoredAccountMeta<'append_vec> {
    pub fn pubkey(&self) -> &'append_vec Pubkey {
        &self.meta.pubkey
    }

    pub fn hash(&self) -> &'append_vec Hash {
        self.hash
    }

    pub fn stored_size(&self) -> usize {
        self.stored_size
    }

    pub fn offset(&self) -> usize {
        self.offset
    }

    pub fn data(&self) -> &'append_vec [u8] {
        self.data
    }

    pub fn data_len(&self) -> u64 {
        self.meta.data_len
    }

    pub fn write_version(&self) -> StoredMetaWriteVersion {
        self.meta.write_version_obsolete
    }

    pub fn meta(&self) -> &StoredMeta {
        self.meta
    }

    pub fn set_meta(&mut self, meta: &'append_vec StoredMeta) {
        self.meta = meta;
    }

    pub(crate) fn sanitize(&self) -> bool {
        self.sanitize_executable() && self.sanitize_lamports()
    }

    fn sanitize_executable(&self) -> bool {
        // Sanitize executable to ensure higher 7-bits are cleared correctly.
        self.ref_executable_byte() & !1 == 0
    }

    fn sanitize_lamports(&self) -> bool {
        // Sanitize 0 lamports to ensure to be same as AccountSharedData::default()
        self.account_meta.lamports != 0
            || self.to_account_shared_data() == AccountSharedData::default()
    }

    fn ref_executable_byte(&self) -> &u8 {
        // Use extra references to avoid value silently clamped to 1 (=true) and 0 (=false)
        // Yes, this really happens; see test_new_from_file_crafted_executable
        let executable_bool: &bool = &self.account_meta.executable;
        // UNSAFE: Force to interpret mmap-backed bool as u8 to really read the actual memory content
        let executable_byte: &u8 = unsafe { &*(executable_bool as *const bool as *const u8) };
        executable_byte
    }
}

impl<'append_vec> ReadableAccount for AppendVecStoredAccountMeta<'append_vec> {
    fn lamports(&self) -> u64 {
        self.account_meta.lamports
    }
    fn data(&self) -> &'append_vec [u8] {
        self.data()
    }
    fn owner(&self) -> &'append_vec Pubkey {
        &self.account_meta.owner
    }
    fn executable(&self) -> bool {
        self.account_meta.executable
    }
    fn rent_epoch(&self) -> Epoch {
        self.account_meta.rent_epoch
    }
}

/// A thread-safe, file-backed block of memory used to store `Account` instances. Append operations
/// are serialized such that only one thread updates the internal `append_lock` at a time. No
/// restrictions are placed on reading. That is, one may read items from one thread while another
/// is appending new items.
#[derive(Debug, AbiExample)]
pub struct AppendVec {
    /// The file path where the data is stored.
    path: PathBuf,

    /// A file-backed block of memory that is used to store the data for each appended item.
    map: MmapMut,

    /// A lock used to serialize append operations.
    append_lock: Mutex<()>,

    /// The number of bytes used to store items, not the number of items.
    current_len: AtomicUsize,

    /// The number of bytes available for storing items.
    file_size: u64,
}

lazy_static! {
    pub static ref APPEND_VEC_MMAPPED_FILES_OPEN: AtomicU64 = AtomicU64::default();
}

impl Drop for AppendVec {
    fn drop(&mut self) {
        APPEND_VEC_MMAPPED_FILES_OPEN.fetch_sub(1, Ordering::Relaxed);
        if let Err(_err) = remove_file(&self.path) {
            // promote this to panic soon.
            // disabled due to many false positive warnings while running tests.
            // blocked by rpc's upgrade to jsonrpc v17
            //error!("AppendVec failed to remove {}: {err}", &self.path.display());
            inc_new_counter_info!("append_vec_drop_fail", 1);
        }
    }
}

impl AppendVec {
    pub fn new(file: &Path, create: bool, size: usize) -> Self {
        let initial_len = 0;
        AppendVec::sanitize_len_and_size(initial_len, size).unwrap();

        if create {
            let _ignored = remove_file(file);
        }

        let mut data = OpenOptions::new()
            .read(true)
            .write(true)
            .create(create)
            .open(file)
            .map_err(|e| {
                panic!(
                    "Unable to {} data file {} in current dir({:?}): {:?}",
                    if create { "create" } else { "open" },
                    file.display(),
                    std::env::current_dir(),
                    e
                );
            })
            .unwrap();

        // Theoretical performance optimization: write a zero to the end of
        // the file so that we won't have to resize it later, which may be
        // expensive.
        data.seek(SeekFrom::Start((size - 1) as u64)).unwrap();
        data.write_all(&[0]).unwrap();
        data.rewind().unwrap();
        data.flush().unwrap();

        //UNSAFE: Required to create a Mmap
        let map = unsafe { MmapMut::map_mut(&data) };
        let map = map.unwrap_or_else(|e| {
            error!(
                "Failed to map the data file (size: {}): {}.\n
                    Please increase sysctl vm.max_map_count or equivalent for your platform.",
                size, e
            );
            std::process::exit(1);
        });
        APPEND_VEC_MMAPPED_FILES_OPEN.fetch_add(1, Ordering::Relaxed);

        AppendVec {
            path: file.to_path_buf(),
            map,
            // This mutex forces append to be single threaded, but concurrent with reads
            // See UNSAFE usage in `append_ptr`
            append_lock: Mutex::new(()),
            current_len: AtomicUsize::new(initial_len),
            file_size: size as u64,
        }
    }

    fn sanitize_len_and_size(current_len: usize, file_size: usize) -> Result<()> {
        if file_size == 0 {
            Err(AccountsFileError::AppendVecError(
                AppendVecError::FileSizeTooSmall(file_size),
            ))
        } else if usize::try_from(MAXIMUM_APPEND_VEC_FILE_SIZE)
            .map(|max| file_size > max)
            .unwrap_or(true)
        {
            Err(AccountsFileError::AppendVecError(
                AppendVecError::FileSizeTooLarge(file_size),
            ))
        } else if current_len > file_size {
            Err(AccountsFileError::AppendVecError(
                AppendVecError::OffsetOutOfBounds(current_len, file_size),
            ))
        } else {
            Ok(())
        }
    }

    pub fn flush(&self) -> Result<()> {
        self.map.flush()?;
        Ok(())
    }

    pub fn reset(&self) {
        // This mutex forces append to be single threaded, but concurrent with reads
        // See UNSAFE usage in `append_ptr`
        let _lock = self.append_lock.lock().unwrap();
        self.current_len.store(0, Ordering::Release);
    }

    /// how many more bytes can be stored in this append vec
    pub fn remaining_bytes(&self) -> u64 {
        (self.capacity()).saturating_sub(self.len() as u64)
    }

    pub fn len(&self) -> usize {
        self.current_len.load(Ordering::Acquire)
    }

    pub fn is_empty(&self) -> bool {
        self.len() == 0
    }

    pub fn capacity(&self) -> u64 {
        self.file_size
    }

    pub fn file_name(slot: Slot, id: impl std::fmt::Display) -> String {
        format!("{slot}.{id}")
    }

    pub fn new_from_file<P: AsRef<Path>>(path: P, current_len: usize) -> Result<(Self, usize)> {
        let new = Self::new_from_file_unchecked(&path, current_len)?;

        let (sanitized, num_accounts) = new.sanitize_layout_and_length();
        if !sanitized {
            // This info show the failing accountvec file path.  It helps debugging
            // the appendvec data corrupution issues related to recycling.
            return Err(AccountsFileError::AppendVecError(
                AppendVecError::IncorrectLayout(path.as_ref().to_path_buf()),
            ));
        }

        Ok((new, num_accounts))
    }

    /// Creates an appendvec from file without performing sanitize checks or counting the number of accounts
    pub fn new_from_file_unchecked<P: AsRef<Path>>(path: P, current_len: usize) -> Result<Self> {
        let file_size = std::fs::metadata(&path)?.len();
        Self::sanitize_len_and_size(current_len, file_size as usize)?;

        let data = OpenOptions::new()
            .read(true)
            .write(true)
            .create(false)
            .open(&path)?;

        let map = unsafe {
            let result = MmapMut::map_mut(&data);
            if result.is_err() {
                // for vm.max_map_count, error is: {code: 12, kind: Other, message: "Cannot allocate memory"}
                info!("memory map error: {:?}. This may be because vm.max_map_count is not set correctly.", result);
            }
            result?
        };
        APPEND_VEC_MMAPPED_FILES_OPEN.fetch_add(1, Ordering::Relaxed);

        Ok(AppendVec {
            path: path.as_ref().to_path_buf(),
            map,
            append_lock: Mutex::new(()),
            current_len: AtomicUsize::new(current_len),
            file_size,
        })
    }

    fn sanitize_layout_and_length(&self) -> (bool, usize) {
        let mut offset = 0;

        // This discards allocated accounts immediately after check at each loop iteration.
        //
        // This code should not reuse AppendVec.accounts() method as the current form or
        // extend it to be reused here because it would allow attackers to accumulate
        // some measurable amount of memory needlessly.
        let mut num_accounts = 0;
        while let Some((account, next_offset)) = self.get_account(offset) {
            if !account.sanitize() {
                return (false, num_accounts);
            }
            offset = next_offset;
            num_accounts += 1;
        }
        let aligned_current_len = u64_align!(self.current_len.load(Ordering::Acquire));

        (offset == aligned_current_len, num_accounts)
    }

    /// Get a reference to the data at `offset` of `size` bytes if that slice
    /// doesn't overrun the internal buffer. Otherwise return None.
    /// Also return the offset of the first byte after the requested data that
    /// falls on a 64-byte boundary.
    fn get_slice(&self, offset: usize, size: usize) -> Option<(&[u8], usize)> {
        let (next, overflow) = offset.overflowing_add(size);
        if overflow || next > self.len() {
            return None;
        }
        let data = &self.map[offset..next];
        let next = u64_align!(next);

        Some((
            //UNSAFE: This unsafe creates a slice that represents a chunk of self.map memory
            //The lifetime of this slice is tied to &self, since it points to self.map memory
            unsafe { std::slice::from_raw_parts(data.as_ptr() as *const u8, size) },
            next,
        ))
    }

    /// Copy `len` bytes from `src` to the first 64-byte boundary after position `offset` of
    /// the internal buffer. Then update `offset` to the first byte after the copied data.
    fn append_ptr(&self, offset: &mut usize, src: *const u8, len: usize) {
        let pos = u64_align!(*offset);
        let data = &self.map[pos..(pos + len)];
        //UNSAFE: This mut append is safe because only 1 thread can append at a time
        //Mutex<()> guarantees exclusive write access to the memory occupied in
        //the range.
        unsafe {
            let dst = data.as_ptr() as *mut u8;
            std::ptr::copy(src, dst, len);
        };
        *offset = pos + len;
    }

    /// Copy each value in `vals`, in order, to the first 64-byte boundary after position `offset`.
    /// If there is sufficient space, then update `offset` and the internal `current_len` to the
    /// first byte after the copied data and return the starting position of the copied data.
    /// Otherwise return None and leave `offset` unchanged.
    fn append_ptrs_locked(&self, offset: &mut usize, vals: &[(*const u8, usize)]) -> Option<usize> {
        let mut end = *offset;
        for val in vals {
            end = u64_align!(end);
            end += val.1;
        }

        if (self.file_size as usize) < end {
            return None;
        }

        let pos = u64_align!(*offset);
        for val in vals {
            self.append_ptr(offset, val.0, val.1)
        }
        self.current_len.store(*offset, Ordering::Release);
        Some(pos)
    }

    /// Return a reference to the type at `offset` if its data doesn't overrun the internal buffer.
    /// Otherwise return None. Also return the offset of the first byte after the requested data
    /// that falls on a 64-byte boundary.
    fn get_type<T>(&self, offset: usize) -> Option<(&T, usize)> {
        let (data, next) = self.get_slice(offset, mem::size_of::<T>())?;
        let ptr: *const T = data.as_ptr() as *const T;
        //UNSAFE: The cast is safe because the slice is aligned and fits into the memory
        //and the lifetime of the &T is tied to self, which holds the underlying memory map
        Some((unsafe { &*ptr }, next))
    }

    /// Return stored account metadata for the account at `offset` if its data doesn't overrun
    /// the internal buffer. Otherwise return None. Also return the offset of the first byte
    /// after the requested data that falls on a 64-byte boundary.
    pub fn get_account(&self, offset: usize) -> Option<(StoredAccountMeta, usize)> {
        let (meta, next): (&StoredMeta, _) = self.get_type(offset)?;
        let (account_meta, next): (&AccountMeta, _) = self.get_type(next)?;
        let (hash, next): (&Hash, _) = self.get_type(next)?;
        let (data, next) = self.get_slice(next, meta.data_len as usize)?;
        let stored_size = next - offset;
        Some((
            StoredAccountMeta::AppendVec(AppendVecStoredAccountMeta {
                meta,
                account_meta,
                data,
                offset,
                stored_size,
                hash,
            }),
            next,
        ))
    }

    fn get_account_meta(&self, offset: usize) -> Option<&AccountMeta> {
        // Skip over StoredMeta data in the account
        let offset = offset.checked_add(mem::size_of::<StoredMeta>())?;
        // u64_align! does an unchecked add for alignment. Check that it won't cause an overflow.
        offset.checked_add(ALIGN_BOUNDARY_OFFSET - 1)?;
        let (account_meta, _): (&AccountMeta, _) = self.get_type(u64_align!(offset))?;
        Some(account_meta)
    }

    /// Return Ok(index_of_matching_owner) if the account owner at `offset` is one of the pubkeys in `owners`.
    /// Return Err(MatchAccountOwnerError::NoMatch) if the account has 0 lamports or the owner is not one of
    /// the pubkeys in `owners`.
    /// Return Err(MatchAccountOwnerError::UnableToLoad) if the `offset` value causes a data overrun.
    pub fn account_matches_owners(
        &self,
        offset: usize,
        owners: &[&Pubkey],
    ) -> std::result::Result<usize, MatchAccountOwnerError> {
        let account_meta = self
            .get_account_meta(offset)
            .ok_or(MatchAccountOwnerError::UnableToLoad)?;
        if account_meta.lamports == 0 {
            Err(MatchAccountOwnerError::NoMatch)
        } else {
            owners
                .iter()
                .position(|entry| &&account_meta.owner == entry)
                .ok_or(MatchAccountOwnerError::NoMatch)
        }
    }

    #[cfg(test)]
    pub fn get_account_test(
        &self,
        offset: usize,
    ) -> Option<(StoredMeta, solana_sdk::account::AccountSharedData)> {
        let (stored_account, _) = self.get_account(offset)?;
        let meta = stored_account.meta().clone();
        Some((meta, stored_account.to_account_shared_data()))
    }

    pub fn get_path(&self) -> PathBuf {
        self.path.clone()
    }

    /// Return iterator for account metadata
    pub fn account_iter(&self) -> AppendVecAccountsIter {
        AppendVecAccountsIter::new(self)
    }

    /// Return a vector of account metadata for each account, starting from `offset`.
    pub fn accounts(&self, mut offset: usize) -> Vec<StoredAccountMeta> {
        let mut accounts = vec![];
        while let Some((account, next)) = self.get_account(offset) {
            accounts.push(account);
            offset = next;
        }
        accounts
    }

    /// Copy each account metadata, account and hash to the internal buffer.
    /// If there is no room to write the first entry, None is returned.
    /// Otherwise, returns the starting offset of each account metadata.
    /// Plus, the final return value is the offset where the next entry would be appended.
    /// So, return.len() is 1 + (number of accounts written)
    /// After each account is appended, the internal `current_len` is updated
    /// and will be available to other threads.
    pub fn append_accounts<
        'a,
        'b,
        T: ReadableAccount + Sync,
        U: StorableAccounts<'a, T>,
        V: Borrow<Hash>,
    >(
        &self,
        accounts: &StorableAccountsWithHashesAndWriteVersions<'a, 'b, T, U, V>,
        skip: usize,
    ) -> Option<Vec<StoredAccountInfo>> {
        let _lock = self.append_lock.lock().unwrap();
        let mut offset = self.len();

        let len = accounts.accounts.len();
        let mut offsets = Vec::with_capacity(len);
        for i in skip..len {
            let (account, pubkey, hash, write_version_obsolete) = accounts.get(i);
            let account_meta = account
                .map(|account| AccountMeta {
                    lamports: account.lamports(),
                    owner: *account.owner(),
                    rent_epoch: account.rent_epoch(),
                    executable: account.executable(),
                })
                .unwrap_or_default();

            let stored_meta = StoredMeta {
                pubkey: *pubkey,
                data_len: account
                    .map(|account| account.data().len())
                    .unwrap_or_default() as u64,
                write_version_obsolete,
            };
            let meta_ptr = &stored_meta as *const StoredMeta;
            let account_meta_ptr = &account_meta as *const AccountMeta;
            let data_len = stored_meta.data_len as usize;
            let data_ptr = account
                .map(|account| account.data())
                .unwrap_or_default()
                .as_ptr();
            let hash_ptr = hash.as_ref().as_ptr();
            let ptrs = [
                (meta_ptr as *const u8, mem::size_of::<StoredMeta>()),
                (account_meta_ptr as *const u8, mem::size_of::<AccountMeta>()),
                (hash_ptr as *const u8, mem::size_of::<Hash>()),
                (data_ptr, data_len),
            ];
            if let Some(res) = self.append_ptrs_locked(&mut offset, &ptrs) {
                offsets.push(res)
            } else {
                break;
            }
        }

        if offsets.is_empty() {
            None
        } else {
            // The last entry in this offset needs to be the u64 aligned offset, because that's
            // where the *next* entry will begin to be stored.
            offsets.push(u64_align!(offset));
            let mut rv = Vec::with_capacity(len);
            for offsets in offsets.windows(2) {
                rv.push(StoredAccountInfo {
                    offset: offsets[0],
                    size: offsets[1] - offsets[0],
                });
            }

            Some(rv)
        }
    }
}

#[cfg(test)]
pub mod tests {
    use {
        super::{test_utils::*, *},
        crate::accounts_db::INCLUDE_SLOT_IN_HASH_TESTS,
        assert_matches::assert_matches,
        memoffset::offset_of,
        rand::{thread_rng, Rng},
        solana_sdk::{
            account::{accounts_equal, Account, AccountSharedData, WritableAccount},
            timing::duration_as_ms,
        },
        std::{mem::ManuallyDrop, time::Instant},
    };

    impl AppendVec {
        pub(crate) fn set_current_len_for_tests(&self, len: usize) {
            self.current_len.store(len, Ordering::Release);
        }

        fn append_account_test(&self, data: &(StoredMeta, AccountSharedData)) -> Option<usize> {
            let slot_ignored = Slot::MAX;
            let accounts = [(&data.0.pubkey, &data.1)];
            let slice = &accounts[..];
            let account_data = (slot_ignored, slice);
            let hash = Hash::default();
            let storable_accounts =
                StorableAccountsWithHashesAndWriteVersions::new_with_hashes_and_write_versions(
                    &account_data,
                    vec![&hash],
                    vec![data.0.write_version_obsolete],
                );

            self.append_accounts(&storable_accounts, 0)
                .map(|res| res[0].offset)
        }
    }

    impl StoredAccountMeta<'_> {
        pub(crate) fn ref_executable_byte(&self) -> &u8 {
            match self {
                Self::AppendVec(av) => av.ref_executable_byte(),
            }
        }
    }

    impl AppendVecStoredAccountMeta<'_> {
        fn set_data_len_unsafe(&self, new_data_len: u64) {
            // UNSAFE: cast away & (= const ref) to &mut to force to mutate append-only (=read-only) AppendVec
            unsafe {
                std::ptr::write(
                    std::mem::transmute::<*const u64, *mut u64>(&self.meta.data_len),
                    new_data_len,
                );
            }
        }

        fn get_executable_byte(&self) -> u8 {
            let executable_bool: bool = self.executable();
            // UNSAFE: Force to interpret mmap-backed bool as u8 to really read the actual memory content
            let executable_byte: u8 = unsafe { std::mem::transmute::<bool, u8>(executable_bool) };
            executable_byte
        }

        fn set_executable_as_byte(&self, new_executable_byte: u8) {
            // UNSAFE: Force to interpret mmap-backed &bool as &u8 to write some crafted value;
            unsafe {
                std::ptr::write(
                    std::mem::transmute::<*const bool, *mut u8>(&self.account_meta.executable),
                    new_executable_byte,
                );
            }
        }
    }

    static_assertions::const_assert_eq!(
        STORE_META_OVERHEAD,
        std::mem::size_of::<StoredMeta>()
            + std::mem::size_of::<AccountMeta>()
            + std::mem::size_of::<Hash>()
    );

    // Hash is [u8; 32], which has no alignment
    static_assertions::assert_eq_align!(u64, StoredMeta, AccountMeta);

    #[test]
    #[should_panic(expected = "assertion failed: accounts.has_hash_and_write_version()")]
    fn test_storable_accounts_with_hashes_and_write_versions_new() {
        let account = AccountSharedData::default();
        // for (Slot, &'a [(&'a Pubkey, &'a T)], IncludeSlotInHash)
        let slot = 0 as Slot;
        let pubkey = Pubkey::default();
        StorableAccountsWithHashesAndWriteVersions::<'_, '_, _, _, &Hash>::new(&(
            slot,
            &[(&pubkey, &account)][..],
            INCLUDE_SLOT_IN_HASH_TESTS,
        ));
    }

    fn test_mismatch(correct_hashes: bool, correct_write_versions: bool) {
        let account = AccountSharedData::default();
        // for (Slot, &'a [(&'a Pubkey, &'a T)], IncludeSlotInHash)
        let slot = 0 as Slot;
        let pubkey = Pubkey::default();
        // mismatch between lens of accounts, hashes, write_versions
        let mut hashes = Vec::default();
        if correct_hashes {
            hashes.push(Hash::default());
        }
        let mut write_versions = Vec::default();
        if correct_write_versions {
            write_versions.push(0);
        }
        StorableAccountsWithHashesAndWriteVersions::new_with_hashes_and_write_versions(
            &(slot, &[(&pubkey, &account)][..], INCLUDE_SLOT_IN_HASH_TESTS),
            hashes,
            write_versions,
        );
    }

    #[test]
    #[should_panic(expected = "assertion failed:")]
    fn test_storable_accounts_with_hashes_and_write_versions_new2() {
        test_mismatch(false, false);
    }

    #[test]
    #[should_panic(expected = "assertion failed:")]
    fn test_storable_accounts_with_hashes_and_write_versions_new3() {
        test_mismatch(false, true);
    }

    #[test]
    #[should_panic(expected = "assertion failed:")]
    fn test_storable_accounts_with_hashes_and_write_versions_new4() {
        test_mismatch(true, false);
    }

    #[test]
    fn test_storable_accounts_with_hashes_and_write_versions_empty() {
        // for (Slot, &'a [(&'a Pubkey, &'a T)], IncludeSlotInHash)
        let account = AccountSharedData::default();
        let slot = 0 as Slot;
        let pubkeys = vec![Pubkey::default()];
        let hashes = Vec::<Hash>::default();
        let write_versions = Vec::default();
        let mut accounts = vec![(&pubkeys[0], &account)];
        accounts.clear();
        let accounts2 = (slot, &accounts[..], INCLUDE_SLOT_IN_HASH_TESTS);
        let storable =
            StorableAccountsWithHashesAndWriteVersions::new_with_hashes_and_write_versions(
                &accounts2,
                hashes,
                write_versions,
            );
        assert_eq!(storable.len(), 0);
        assert!(storable.is_empty());
    }

    #[test]
    fn test_storable_accounts_with_hashes_and_write_versions_hash_and_write_version() {
        // for (Slot, &'a [(&'a Pubkey, &'a T)], IncludeSlotInHash)
        let account = AccountSharedData::default();
        let slot = 0 as Slot;
        let pubkeys = vec![Pubkey::from([5; 32]), Pubkey::from([6; 32])];
        let hashes = vec![Hash::new(&[3; 32]), Hash::new(&[4; 32])];
        let write_versions = vec![42, 43];
        let accounts = vec![(&pubkeys[0], &account), (&pubkeys[1], &account)];
        let accounts2 = (slot, &accounts[..], INCLUDE_SLOT_IN_HASH_TESTS);
        let storable =
            StorableAccountsWithHashesAndWriteVersions::new_with_hashes_and_write_versions(
                &accounts2,
                hashes.clone(),
                write_versions.clone(),
            );
        assert_eq!(storable.len(), pubkeys.len());
        assert!(!storable.is_empty());
        (0..2).for_each(|i| {
            let (_, pubkey, hash, write_version) = storable.get(i);
            assert_eq!(hash, &hashes[i]);
            assert_eq!(write_version, write_versions[i]);
            assert_eq!(pubkey, &pubkeys[i]);
        });
    }

    #[test]
    fn test_storable_accounts_with_hashes_and_write_versions_default() {
        // 0 lamport account, should return default account (or None in this case)
        let account = Account {
            data: vec![0],
            ..Account::default()
        }
        .to_account_shared_data();
        // for (Slot, &'a [(&'a Pubkey, &'a T)], IncludeSlotInHash)
        let slot = 0 as Slot;
        let pubkey = Pubkey::default();
        let hashes = vec![Hash::default()];
        let write_versions = vec![0];
        let accounts = vec![(&pubkey, &account)];
        let accounts2 = (slot, &accounts[..], INCLUDE_SLOT_IN_HASH_TESTS);
        let storable =
            StorableAccountsWithHashesAndWriteVersions::new_with_hashes_and_write_versions(
                &accounts2,
                hashes.clone(),
                write_versions.clone(),
            );
        let get_account = storable.account(0);
        assert!(get_account.is_none());

        // non-zero lamports, data should be correct
        let account = Account {
            lamports: 1,
            data: vec![0],
            ..Account::default()
        }
        .to_account_shared_data();
        // for (Slot, &'a [(&'a Pubkey, &'a T)], IncludeSlotInHash)
        let accounts = vec![(&pubkey, &account)];
        let accounts2 = (slot, &accounts[..], INCLUDE_SLOT_IN_HASH_TESTS);
        let storable =
            StorableAccountsWithHashesAndWriteVersions::new_with_hashes_and_write_versions(
                &accounts2,
                hashes,
                write_versions,
            );
        let get_account = storable.account(0);
        assert!(accounts_equal(&account, get_account.unwrap()));
    }

    #[test]
    fn test_account_meta_default() {
        let def1 = AccountMeta::default();
        let def2 = AccountMeta::from(&Account::default());
        assert_eq!(&def1, &def2);
        let def2 = AccountMeta::from(&AccountSharedData::default());
        assert_eq!(&def1, &def2);
        let def2 = AccountMeta::from(Some(&AccountSharedData::default()));
        assert_eq!(&def1, &def2);
        let none: Option<&AccountSharedData> = None;
        let def2 = AccountMeta::from(none);
        assert_eq!(&def1, &def2);
    }

    #[test]
    fn test_account_meta_non_default() {
        let def1 = AccountMeta {
            lamports: 1,
            owner: Pubkey::new_unique(),
            executable: true,
            rent_epoch: 3,
        };
        let def2_account = Account {
            lamports: def1.lamports,
            owner: def1.owner,
            executable: def1.executable,
            rent_epoch: def1.rent_epoch,
            data: Vec::new(),
        };
        let def2 = AccountMeta::from(&def2_account);
        assert_eq!(&def1, &def2);
        let def2 = AccountMeta::from(&AccountSharedData::from(def2_account.clone()));
        assert_eq!(&def1, &def2);
        let def2 = AccountMeta::from(Some(&AccountSharedData::from(def2_account)));
        assert_eq!(&def1, &def2);
    }

    #[test]
    #[should_panic(expected = "AppendVecError(FileSizeTooSmall(0))")]
    fn test_append_vec_new_bad_size() {
        let path = get_append_vec_path("test_append_vec_new_bad_size");
        let _av = AppendVec::new(&path.path, true, 0);
    }

    #[test]
    fn test_append_vec_new_from_file_bad_size() {
        let file = get_append_vec_path("test_append_vec_new_from_file_bad_size");
        let path = &file.path;

        let _data = OpenOptions::new()
            .read(true)
            .write(true)
            .create(true)
            .open(path)
            .expect("create a test file for mmap");

        let result = AppendVec::new_from_file(path, 0);
        assert_matches!(result, Err(ref message) if message.to_string().contains("too small file size 0 for AppendVec"));
    }

    #[test]
    fn test_append_vec_sanitize_len_and_size_too_small() {
        const LEN: usize = 0;
        const SIZE: usize = 0;
        let result = AppendVec::sanitize_len_and_size(LEN, SIZE);
        assert_matches!(result, Err(ref message) if message.to_string().contains("too small file size 0 for AppendVec"));
    }

    #[test]
    fn test_append_vec_sanitize_len_and_size_maximum() {
        const LEN: usize = 0;
        const SIZE: usize = 16 * 1024 * 1024 * 1024;
        let result = AppendVec::sanitize_len_and_size(LEN, SIZE);
        assert_matches!(result, Ok(_));
    }

    #[test]
    fn test_append_vec_sanitize_len_and_size_too_large() {
        const LEN: usize = 0;
        const SIZE: usize = 16 * 1024 * 1024 * 1024 + 1;
        let result = AppendVec::sanitize_len_and_size(LEN, SIZE);
        assert_matches!(result, Err(ref message) if message.to_string().contains("too large file size 17179869185 for AppendVec"));
    }

    #[test]
    fn test_append_vec_sanitize_len_and_size_full_and_same_as_current_len() {
        const LEN: usize = 1024 * 1024;
        const SIZE: usize = 1024 * 1024;
        let result = AppendVec::sanitize_len_and_size(LEN, SIZE);
        assert_matches!(result, Ok(_));
    }

    #[test]
    fn test_append_vec_sanitize_len_and_size_larger_current_len() {
        const LEN: usize = 1024 * 1024 + 1;
        const SIZE: usize = 1024 * 1024;
        let result = AppendVec::sanitize_len_and_size(LEN, SIZE);
        assert_matches!(result, Err(ref message) if message.to_string().contains("is larger than file size (1048576)"));
    }

    #[test]
    fn test_append_vec_one() {
        let path = get_append_vec_path("test_append");
        let av = AppendVec::new(&path.path, true, 1024 * 1024);
        let account = create_test_account(0);
        let index = av.append_account_test(&account).unwrap();
        assert_eq!(av.get_account_test(index).unwrap(), account);
    }

    #[test]
    fn test_remaining_bytes() {
        let path = get_append_vec_path("test_append");
        let sz = 1024 * 1024;
        let sz64 = sz as u64;
        let av = AppendVec::new(&path.path, true, sz);
        assert_eq!(av.capacity(), sz64);
        assert_eq!(av.remaining_bytes(), sz64);
        let account = create_test_account(0);
        av.append_account_test(&account).unwrap();
        assert_eq!(av.capacity(), sz64);
        assert_eq!(av.remaining_bytes(), sz64 - (STORE_META_OVERHEAD as u64));
    }

    #[test]
    fn test_append_vec_data() {
        let path = get_append_vec_path("test_append_data");
        let av = AppendVec::new(&path.path, true, 1024 * 1024);
        let account = create_test_account(5);
        let index = av.append_account_test(&account).unwrap();
        assert_eq!(av.get_account_test(index).unwrap(), account);
        let account1 = create_test_account(6);
        let index1 = av.append_account_test(&account1).unwrap();
        assert_eq!(av.get_account_test(index).unwrap(), account);
        assert_eq!(av.get_account_test(index1).unwrap(), account1);
    }

    #[test]
    fn test_account_matches_owners() {
        let path = get_append_vec_path("test_append_data");
        let av = AppendVec::new(&path.path, true, 1024 * 1024);
        let owners: Vec<Pubkey> = (0..2).map(|_| Pubkey::new_unique()).collect();
        let owners_refs: Vec<&Pubkey> = owners.iter().collect();

        let mut account = create_test_account(5);
        account.1.set_owner(owners[0]);
        let index = av.append_account_test(&account).unwrap();
        assert_eq!(av.account_matches_owners(index, &owners_refs), Ok(0));

        let mut account1 = create_test_account(6);
        account1.1.set_owner(owners[1]);
        let index1 = av.append_account_test(&account1).unwrap();
        assert_eq!(av.account_matches_owners(index1, &owners_refs), Ok(1));
        assert_eq!(av.account_matches_owners(index, &owners_refs), Ok(0));

        let mut account2 = create_test_account(6);
        account2.1.set_owner(Pubkey::new_unique());
        let index2 = av.append_account_test(&account2).unwrap();
        assert_eq!(
            av.account_matches_owners(index2, &owners_refs),
            Err(MatchAccountOwnerError::NoMatch)
        );

        // tests for overflow
        assert_eq!(
            av.account_matches_owners(usize::MAX - mem::size_of::<StoredMeta>(), &owners_refs),
            Err(MatchAccountOwnerError::UnableToLoad)
        );

        assert_eq!(
            av.account_matches_owners(
                usize::MAX - mem::size_of::<StoredMeta>() - mem::size_of::<AccountMeta>() + 1,
                &owners_refs
            ),
            Err(MatchAccountOwnerError::UnableToLoad)
        );
    }

    #[test]
    fn test_append_vec_append_many() {
        let path = get_append_vec_path("test_append_many");
        let av = AppendVec::new(&path.path, true, 1024 * 1024);
        let size = 1000;
        let mut indexes = vec![];
        let now = Instant::now();
        for sample in 0..size {
            let account = create_test_account(sample);
            let pos = av.append_account_test(&account).unwrap();
            assert_eq!(av.get_account_test(pos).unwrap(), account);
            indexes.push(pos)
        }
        trace!("append time: {} ms", duration_as_ms(&now.elapsed()),);

        let now = Instant::now();
        for _ in 0..size {
            let sample = thread_rng().gen_range(0, indexes.len());
            let account = create_test_account(sample);
            assert_eq!(av.get_account_test(indexes[sample]).unwrap(), account);
        }
        trace!("random read time: {} ms", duration_as_ms(&now.elapsed()),);

        let now = Instant::now();
        assert_eq!(indexes.len(), size);
        assert_eq!(indexes[0], 0);
        let mut accounts = av.accounts(indexes[0]);
        assert_eq!(accounts.len(), size);
        for (sample, v) in accounts.iter_mut().enumerate() {
            let account = create_test_account(sample);
            let recovered = v.to_account_shared_data();
            assert_eq!(recovered, account.1)
        }
        trace!(
            "sequential read time: {} ms",
            duration_as_ms(&now.elapsed()),
        );
    }

    #[test]
    fn test_new_from_file_crafted_zero_lamport_account() {
        // This test verifies that when we sanitize on load, that we fail sanitizing if we load an account with zero lamports that does not have all default value fields.
        // This test writes an account with zero lamports, but with 3 bytes of data. On load, it asserts that load fails.
        // It used to be possible to use the append vec api to write an account to an append vec with zero lamports, but with non-default values for other account fields.
        // This will no longer be possible. Thus, to implement the write portion of this test would require additional test-only parameters to public apis or otherwise duplicating code paths.
        // So, the sanitizing on load behavior can be tested by capturing [u8] that would be created if such a write was possible (as it used to be).
        // The contents of [u8] written by an append vec cannot easily or reasonably change frequently since it has released a long time.
        /*
            solana_logger::setup();
            // uncomment this code to generate the invalid append vec that will fail on load
            let file = get_append_vec_path("test_append");
            let path = &file.path;
            let mut av = AppendVec::new(path, true, 256);
            av.set_no_remove_on_drop();

            let pubkey = solana_sdk::pubkey::new_rand();
            let owner = Pubkey::default();
            let data_len = 3_u64;
            let mut account = AccountSharedData::new(0, data_len as usize, &owner);
            account.set_data(b"abc".to_vec());
            let stored_meta = StoredMeta {
                write_version: 0,
                pubkey,
                data_len,
            };
            let account_with_meta = (stored_meta, account);
            let index = av.append_account_test(&account_with_meta).unwrap();
            assert_eq!(av.get_account_test(index).unwrap(), account_with_meta);

            av.flush().unwrap();
            let accounts_len = av.len();
            drop(av);
            // read file and log out as [u8]
            use std::fs::File;
            use std::io::BufReader;
            use std::io::Read;
            let f = File::open(path).unwrap();
            let mut reader = BufReader::new(f);
            let mut buffer = Vec::new();
            reader.read_to_end(&mut buffer).unwrap();
            error!("{:?}", buffer);
        */

        // create an invalid append vec file using known bytes
        let file = get_append_vec_path("test_append_bytes");
        let path = &file.path;

        let accounts_len = 139;
        {
            let append_vec_data = [
                0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 192, 118, 150, 1, 185, 209, 118,
                82, 154, 222, 172, 202, 110, 26, 218, 140, 143, 96, 61, 43, 212, 73, 203, 7, 190,
                88, 80, 222, 110, 114, 67, 254, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 97, 98, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            ];

            let f = std::fs::File::create(path).unwrap();
            let mut writer = std::io::BufWriter::new(f);
            writer.write_all(append_vec_data.as_slice()).unwrap();
        }

        let result = AppendVec::new_from_file(path, accounts_len);
        assert_matches!(result, Err(ref message) if message.to_string().contains("incorrect layout/length/data"));
    }

    #[test]
    fn test_new_from_file_crafted_data_len() {
        let file = get_append_vec_path("test_new_from_file_crafted_data_len");
        let path = &file.path;
        let accounts_len = {
            // wrap AppendVec in ManuallyDrop to ensure we do not remove the backing file when dropped
            let av = ManuallyDrop::new(AppendVec::new(path, true, 1024 * 1024));

            let crafted_data_len = 1;

            av.append_account_test(&create_test_account(10)).unwrap();

            let accounts = av.accounts(0);
            let StoredAccountMeta::AppendVec(account) = accounts.first().unwrap();
            account.set_data_len_unsafe(crafted_data_len);
            assert_eq!(account.data_len(), crafted_data_len);

            // Reload accounts and observe crafted_data_len
            let accounts = av.accounts(0);
            let account = accounts.first().unwrap();
            assert_eq!(account.data_len(), crafted_data_len);

            av.flush().unwrap();
            av.len()
        };
        let result = AppendVec::new_from_file(path, accounts_len);
        assert_matches!(result, Err(ref message) if message.to_string().contains("incorrect layout/length/data"));
    }

    #[test]
    fn test_new_from_file_too_large_data_len() {
        let file = get_append_vec_path("test_new_from_file_too_large_data_len");
        let path = &file.path;
        let accounts_len = {
            // wrap AppendVec in ManuallyDrop to ensure we do not remove the backing file when dropped
            let av = ManuallyDrop::new(AppendVec::new(path, true, 1024 * 1024));

            let too_large_data_len = u64::max_value();
            av.append_account_test(&create_test_account(10)).unwrap();

            let accounts = av.accounts(0);
            let StoredAccountMeta::AppendVec(account) = accounts.first().unwrap();
            account.set_data_len_unsafe(too_large_data_len);
            assert_eq!(account.data_len(), too_large_data_len);

            // Reload accounts and observe no account with bad offset
            let accounts = av.accounts(0);
            assert_matches!(accounts.first(), None);

            av.flush().unwrap();
            av.len()
        };
        let result = AppendVec::new_from_file(path, accounts_len);
        assert_matches!(result, Err(ref message) if message.to_string().contains("incorrect layout/length/data"));
    }

    #[test]
    fn test_new_from_file_crafted_executable() {
        let file = get_append_vec_path("test_new_from_crafted_executable");
        let path = &file.path;
        let accounts_len = {
            // wrap AppendVec in ManuallyDrop to ensure we do not remove the backing file when dropped
            let av = ManuallyDrop::new(AppendVec::new(path, true, 1024 * 1024));
            av.append_account_test(&create_test_account(10)).unwrap();
            {
                let mut executable_account = create_test_account(10);
                executable_account.1.set_executable(true);
                av.append_account_test(&executable_account).unwrap();
            }

            // reload accounts
            let accounts = av.accounts(0);

            // ensure false is 0u8 and true is 1u8 actually
            assert_eq!(*accounts[0].ref_executable_byte(), 0);
            assert_eq!(*accounts[1].ref_executable_byte(), 1);

            let StoredAccountMeta::AppendVec(account) = &accounts[0];
            let crafted_executable = u8::max_value() - 1;

            account.set_executable_as_byte(crafted_executable);

            // reload crafted accounts
            let accounts = av.accounts(0);
            let StoredAccountMeta::AppendVec(account) = accounts.first().unwrap();

            // upper 7-bits are not 0, so sanitization should fail
            assert!(!account.sanitize_executable());

            // we can observe crafted value by ref
            {
                let executable_bool: &bool = &account.account_meta.executable;
                // Depending on use, *executable_bool can be truthy or falsy due to direct memory manipulation
                // assert_eq! thinks *executable_bool is equal to false but the if condition thinks it's not, contradictorily.
                assert!(!*executable_bool);
                #[cfg(not(target_arch = "aarch64"))]
                {
                    const FALSE: bool = false; // keep clippy happy
                    if *executable_bool == FALSE {
                        panic!("This didn't occur if this test passed.");
                    }
                }
                assert_eq!(*account.ref_executable_byte(), crafted_executable);
            }

            // we can NOT observe crafted value by value
            {
                let executable_bool: bool = account.executable();
                assert!(!executable_bool);
                assert_eq!(account.get_executable_byte(), 0); // Wow, not crafted_executable!
            }

            av.flush().unwrap();
            av.len()
        };
        let result = AppendVec::new_from_file(path, accounts_len);
        assert_matches!(result, Err(ref message) if message.to_string().contains("incorrect layout/length/data"));
    }

    #[test]
    fn test_type_layout() {
        assert_eq!(offset_of!(StoredMeta, write_version_obsolete), 0x00);
        assert_eq!(offset_of!(StoredMeta, data_len), 0x08);
        assert_eq!(offset_of!(StoredMeta, pubkey), 0x10);
        assert_eq!(mem::size_of::<StoredMeta>(), 0x30);

        assert_eq!(offset_of!(AccountMeta, lamports), 0x00);
        assert_eq!(offset_of!(AccountMeta, rent_epoch), 0x08);
        assert_eq!(offset_of!(AccountMeta, owner), 0x10);
        assert_eq!(offset_of!(AccountMeta, executable), 0x30);
        assert_eq!(mem::size_of::<AccountMeta>(), 0x38);
    }
}


