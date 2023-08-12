programs/token-metadata/program/src/processor/edition/mod.rs
============================================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: rs

    mod convert_master_edition_v1_to_v2;
mod create_master_edition_v3;
mod mint_new_edition_from_master_edition_via_token;

pub use convert_master_edition_v1_to_v2::*;
pub use create_master_edition_v3::*;
pub use mint_new_edition_from_master_edition_via_token::*;


