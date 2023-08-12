programs/realm-voter/src/state/mod.rs
=====================================

Last edited: 2023-06-01 19:30:16

Contents:

.. code-block:: rs

    pub use registrar::*;
pub mod registrar;

pub use governance_program_config::*;
pub mod governance_program_config;

pub mod max_voter_weight_record;

pub use voter_weight_record::*;
pub mod voter_weight_record;


