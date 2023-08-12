programs/dummy-oracle/src/instruction.rs
========================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: rs

    pub use crate::processor::{initialize_clock, initialize_oracle, update_clock, update_price};
use borsh::{BorshDeserialize, BorshSerialize};

#[derive(BorshSerialize, BorshDeserialize, Clone)]
pub enum DummyInstruction {
    InitializeClock(initialize_clock::Params),

    InitializeOracle(initialize_oracle::Params),

    UpdateClock(update_clock::Params),

    UpdatePrice(update_price::Params),
}


