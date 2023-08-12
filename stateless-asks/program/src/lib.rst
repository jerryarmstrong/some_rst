stateless-asks/program/src/lib.rs
=================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: rs

    pub mod error;
pub mod instruction;
pub mod processor;
pub mod validation_utils;

#[cfg(not(feature = "no-entrypoint"))]
mod entrypoint;

// Export current sdk types for downstream users building with a different sdk version
pub use solana_program;


