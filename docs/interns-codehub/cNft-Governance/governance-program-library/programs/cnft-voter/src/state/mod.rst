cNft-Governance/governance-program-library/programs/cnft-voter/src/state/mod.rs
===============================================================================

Last edited: 2023-07-14 15:51:14

Contents:

.. code-block:: rs

    pub use registrar::*;
pub mod registrar;

pub use collection_config::*;
pub mod collection_config;

pub use voter_weight_record::*;
pub mod voter_weight_record;

pub use max_voter_weight_record::*;
pub mod max_voter_weight_record;

pub use cnft_vote_record::*;
pub mod cnft_vote_record;

pub use cnft_verification::*;
pub mod cnft_verification;

pub use metaplex_adapter::*;
pub mod metaplex_adapter;

pub mod idl_types;

