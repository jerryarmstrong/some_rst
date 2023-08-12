program/src/state.rs
====================

Last edited: 2023-04-22 23:05:55

Contents:

.. code-block:: rs

    use borsh::{BorshDeserialize, BorshSerialize};
use shank::ShankAccount;

#[repr(C)]
#[derive(Clone, BorshSerialize, BorshDeserialize, Debug, ShankAccount)]
pub struct AccountThingy {
    thing: u8,
}


