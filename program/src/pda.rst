program/src/pda.rs
==================

Last edited: 2023-08-01 14:25:31

Contents:

.. code-block:: rs

    use super::*;

pub fn find_rooster_pda(authority: &Pubkey) -> (Pubkey, u8) {
    let seeds = &[b"rooster", authority.as_ref()];
    Pubkey::find_program_address(seeds, &crate::ID)
}


