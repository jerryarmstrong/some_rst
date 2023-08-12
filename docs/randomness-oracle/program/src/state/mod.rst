program/src/state/mod.rs
========================

Last edited: 2021-12-14 12:31:39

Contents:

.. code-block:: rs

    //! State types.

mod randomness_oracle;

use borsh::{BorshDeserialize, BorshSchema, BorshSerialize};
pub use randomness_oracle::*;

/// Enum representing the account type managed by the program
#[derive(Clone, Debug, PartialEq, BorshDeserialize, BorshSerialize, BorshSchema)]
pub enum AccountType {
    /// If the account has not been initialized, the enum will be 0
    Uninitialized,
    /// Random oracle
    RandomnessOracle,
}

impl Default for AccountType {
    fn default() -> Self {
        AccountType::Uninitialized
    }
}


