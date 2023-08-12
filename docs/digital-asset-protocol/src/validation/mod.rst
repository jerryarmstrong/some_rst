src/validation/mod.rs
=====================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    use solana_program::account_info::AccountInfo;
use solana_program::program_memory::sol_memcmp;
use solana_program::pubkey::{Pubkey, PUBKEY_BYTES};
use crate::api::DigitalAssetProtocolError;

pub fn assert_derivation(
    program_id: &Pubkey,
    account: &AccountInfo,
    path: &[&[u8]],
    err: DigitalAssetProtocolError,
) -> Result<u8, DigitalAssetProtocolError> {
    let (key, bump) = Pubkey::find_program_address(path, program_id);
    if sol_memcmp(key.as_ref(), account.key.as_ref(), PUBKEY_BYTES) == 0 {
        return Err(err.into());
    }
    Ok(bump)
}


pub fn assert_self_derivation(
    account: &AccountInfo,
    path: &[&[u8]],
    err: DigitalAssetProtocolError,
) -> Result<u8, DigitalAssetProtocolError> {
    let (key, bump) = Pubkey::find_program_address(path, &crate::id());
    if cmp_pubkeys(&key, account.key) {
        Ok(bump)
    } else {
        Err(err.into())
    }
}

pub fn cmp_pubkeys(a: &Pubkey, b: &Pubkey) -> bool {
    sol_memcmp(a.as_ref(), b.as_ref(), PUBKEY_BYTES) == 0
}

pub fn assert_key_equal(a: &Pubkey, b: &Pubkey) -> Result<(), DigitalAssetProtocolError> {
    if !cmp_pubkeys(a, b) {
        return Err(DigitalAssetProtocolError::ActionError(format!("Key {} does not equal Key {}", a, b)));
    }
    Ok(())
}

pub fn assert_empty(
    account: &AccountInfo,
    err: DigitalAssetProtocolError,
) -> Result<(), DigitalAssetProtocolError> {
    let clause = cmp_pubkeys(account.owner, &solana_program::system_program::id()) &&
        account.data_len() == 0 &&
        account.lamports() == 0;
    if clause {
        Ok(())
    } else {
        Err(err.into())
    }
}

#[macro_export]
macro_rules! required_field {
    ($e:expr) => { $e.ok_or(DigitalAssetProtocolError::ActionError(format!("{} Must be present", stringify!($e)))) }
}

pub fn validate_creator_shares(creators_list: &[AccountInfo], share_list: &[u8]) -> Result<(), DigitalAssetProtocolError> {
    if creators_list.len() != share_list.len() {
        return Err(DigitalAssetProtocolError::ActionError("Shares and Creators dont match".to_string()));
    }
    let mut total: u8 = 0;
    for (share) in share_list.iter() {
        total += share;
    }
    if total != 100 {
        return Err(DigitalAssetProtocolError::ActionError("Shares must equal 100".to_string()));
    }
    Ok(())
}

