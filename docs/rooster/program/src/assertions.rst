program/src/assertions.rs
=========================

Last edited: 2023-08-01 14:25:31

Contents:

.. code-block:: rs

    use crate::pda::find_rooster_pda;

use super::*;

pub fn assert_rooster_pda(
    account_info: &AccountInfo,
    authority_info: &AccountInfo,
) -> Result<u8, ProgramError> {
    let (pubkey, bump) = find_rooster_pda(authority_info.key);

    if pubkey != *account_info.key {
        return Err(Crows::RoosterPDAInvalid.into());
    }

    Ok(bump)
}


