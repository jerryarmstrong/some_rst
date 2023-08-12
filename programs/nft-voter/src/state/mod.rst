programs/nft-voter/src/state/mod.rs
===================================

Last edited: 2023-06-01 19:30:16

Contents:

.. code-block:: rs

    pub use registrar::*;
pub mod registrar;

pub use collection_config::*;
pub mod collection_config;

pub use nft_vote_record::*;
pub mod nft_vote_record;

pub mod max_voter_weight_record;

pub use voter_weight_record::*;
pub mod voter_weight_record;

pub mod idl_types;


