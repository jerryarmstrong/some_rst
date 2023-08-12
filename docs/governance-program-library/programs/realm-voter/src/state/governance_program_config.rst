programs/realm-voter/src/state/governance_program_config.rs
===========================================================

Last edited: 2023-06-01 19:30:16

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;

/// Configuration of an spl-governance instance used to grant governance power
#[derive(AnchorSerialize, AnchorDeserialize, Debug, Clone, Copy, PartialEq, Default)]
pub struct GovernanceProgramConfig {
    /// The program id of the configured spl-governance instance
    pub program_id: Pubkey,

    /// Reserved for future upgrades
    pub reserved: [u8; 8],
}


