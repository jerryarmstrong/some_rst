sdk/program/src/nonce/mod.rs
============================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    //! Durable transaction nonces.

pub mod state;
pub use state::State;

pub const NONCED_TX_MARKER_IX_INDEX: u8 = 0;


