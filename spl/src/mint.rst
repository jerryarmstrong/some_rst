spl/src/mint.rs
===============

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: rs

    use anchor_lang::solana_program::declare_id;

pub use srm::ID as SRM;
mod srm {
    use super::*;
    declare_id!("SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt");
}

pub use usdc::ID as USDC;
mod usdc {
    use super::*;
    declare_id!("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v");
}


