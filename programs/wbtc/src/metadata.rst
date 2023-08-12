programs/wbtc/src/metadata.rs
=============================

Last edited: 2023-06-16 20:26:13

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

use mpl_token_metadata::ID;

#[derive(Clone)]
pub struct MetadataProgram;

impl anchor_lang::Id for MetadataProgram {
    fn id() -> Pubkey {
        ID
    }
}


