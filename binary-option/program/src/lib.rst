binary-option/program/src/lib.rs
================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    pub mod entrypoint;
pub mod error;
pub mod instruction;
pub mod processor;
pub mod spl_utils;
pub mod state;
pub mod system_utils;
pub mod validation_utils;
// Export current sdk types for downstream users building with a different sdk version
pub use solana_program;

solana_program::declare_id!("betw959P4WToez4DkuXwNsJszqbpe3HuY56AcG5yevx");


