programs/cardinal-stake-pool/src/instructions/mod.rs
====================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    pub mod authorize_mint;
pub mod claim_receipt_mint;
pub mod claim_stake_entry_funds;
pub mod close_stake_entry;
pub mod close_stake_pool;
pub mod deauthorize_mint;
pub mod double_or_reset_total_stake_seconds;
pub mod init_entry;
pub mod init_identifier;
pub mod init_pool;
pub mod init_stake_mint;
pub mod reassign_stake_entry;
pub mod reset_stake_entry_bump;
pub mod return_receipt_mint;
pub mod stake;
pub mod stake_entry_fill_zeros;
pub mod stake_entry_resize;
pub mod stake_pool_fill_zeros;
pub mod unstake;
pub mod update_pool;
pub mod update_total_stake_seconds;

pub use authorize_mint::*;
pub use claim_receipt_mint::*;
pub use claim_stake_entry_funds::*;
pub use close_stake_entry::*;
pub use close_stake_pool::*;
pub use deauthorize_mint::*;
pub use double_or_reset_total_stake_seconds::*;
pub use init_entry::*;
pub use init_identifier::*;
pub use init_pool::*;
pub use init_stake_mint::*;
pub use reassign_stake_entry::*;
pub use reset_stake_entry_bump::*;
pub use return_receipt_mint::*;
pub use stake::*;
pub use stake_entry_fill_zeros::*;
pub use stake_entry_resize::*;
pub use stake_pool_fill_zeros::*;
pub use unstake::*;
pub use update_pool::*;
pub use update_total_stake_seconds::*;

// programmable
pub mod programmable;
pub use programmable::stake_programmable::*;
pub use programmable::unstake_custodial_programmable::*;
pub use programmable::unstake_programmable::*;

// stake_booster
pub mod stake_booster;
pub use stake_booster::boost_stake_entry::*;
pub use stake_booster::close_stake_booster::*;
pub use stake_booster::init_stake_booster::*;
pub use stake_booster::update_stake_booster::*;

// groups
pub mod groups;
pub use groups::add_to_group_entry::*;
pub use groups::init_group_entry::*;
pub use groups::init_ungrouping::*;
pub use groups::remove_from_group_entry::*;


