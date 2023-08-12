cNft-Governance/governance-program-library/programs/cnft-voter/src/instructions/mod.rs
======================================================================================

Last edited: 2023-07-14 15:51:14

Contents:

.. code-block:: rs

    pub use create_registrar::*;
mod create_registrar;

pub use create_voter_weight_record::*;
mod create_voter_weight_record;

pub use create_max_voter_weight_record::*;
mod create_max_voter_weight_record;

pub use update_voter_weight_record::*;
mod update_voter_weight_record;

pub use relinquish_cnft_vote::*;
mod relinquish_cnft_vote;

pub use configure_collection::*;
mod configure_collection;

pub use cast_cnft_vote::*;
mod cast_cnft_vote;

pub use verify_cnft_info::*;
mod verify_cnft_info;

