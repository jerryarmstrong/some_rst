program/src/state.rs
====================

Last edited: 2023-08-01 14:25:31

Contents:

.. code-block:: rs

    use borsh::{BorshDeserialize, BorshSerialize};
use shank::ShankAccount;

#[repr(C)]
#[derive(Clone, BorshSerialize, BorshDeserialize, Debug, ShankAccount)]
pub struct Rooster {
    bump: u8,
}

impl Rooster {
    pub fn new(bump: u8) -> Self {
        Self { bump }
    }
}


