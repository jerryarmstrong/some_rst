programs/realm-voter/src/instructions/mod.rs
============================================

Last edited: 2023-06-01 19:30:16

Contents:

.. code-block:: rs

    pub use configure_governance_program::*;
mod configure_governance_program;

pub use create_registrar::*;
mod create_registrar;

pub use create_voter_weight_record::*;
mod create_voter_weight_record;

pub use create_max_voter_weight_record::*;
mod create_max_voter_weight_record;

pub use update_voter_weight_record::*;
mod update_voter_weight_record;

pub use configure_voter_weights::*;
mod configure_voter_weights;


