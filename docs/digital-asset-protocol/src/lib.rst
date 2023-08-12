src/lib.rs
==========

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    mod api;
mod entrypoint;
mod interfaces;
mod lifecycle;
mod generated;
mod modules;
pub mod blob;
pub mod module;

#[macro_use]
pub mod validation;

pub use solana_program;

solana_program::declare_id!("assetbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s");


