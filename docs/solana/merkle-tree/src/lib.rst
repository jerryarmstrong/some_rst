merkle-tree/src/lib.rs
======================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    #![allow(clippy::integer_arithmetic)]

#[cfg(target_os = "solana")]
#[macro_use]
extern crate matches;

pub mod merkle_tree;
pub use merkle_tree::MerkleTree;


