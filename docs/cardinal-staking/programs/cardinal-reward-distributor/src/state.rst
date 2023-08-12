programs/cardinal-reward-distributor/src/state.rs
=================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey;
use std::str::FromStr;

// Re-export.
pub use cardinal_stake_pool::state::INIT_AUTHORITY;

pub const CLAIM_REWARD_LAMPORTS: u64 = 2_000_000;

pub fn assert_reward_manager(pubkey: &Pubkey) -> bool {
    pubkey.to_string() == Pubkey::from_str("crkdpVWjHWdggGgBuSyAqSmZUmAjYLzD435tcLDRLXr").unwrap().to_string()
}

pub const REWARD_ENTRY_SEED: &str = "reward-entry";

////////////////////////////////////////////////////////////////////////////////
// If any of these three change, we need to update the tests in the
// soulbound repo.
////////////////////////////////////////////////////////////////////////////////

// Program id of the souldbound program.
pub const SBA_PROGRAM: Pubkey = pubkey!("7DkjPwuKxvz6Viiawtbmb4CqnMKP6eGb1WqYas1airUS");

// PDA namespace prefix for the souldbound authority for this staking program.
pub const NS_SBA_SCOPED_USER_NFT_PROGRAM: &[u8] = b"sba-scoped-user-nft-program";

////////////////////////////////////////////////////////////////////////////////

pub const REWARD_ENTRY_SIZE: usize = 8 + std::mem::size_of::<RewardEntry>() + 64;
#[account]
pub struct RewardEntry {
    pub bump: u8,
    pub stake_entry: Pubkey,
    pub reward_distributor: Pubkey,
    pub reward_seconds_received: u128,
    pub multiplier: u64,
}

#[derive(Clone, Debug, PartialEq, Eq, AnchorSerialize, AnchorDeserialize)]
#[repr(u8)]
pub enum RewardDistributorKind {
    /// Rewards are distributed by minting new tokens
    Mint = 1,
    /// Rewards are distributed from a treasury
    Treasury = 2,
}

pub const REWARD_DISTRIBUTOR_SEED: &str = "reward-distributor";
pub const REWARD_DISTRIBUTOR_SIZE: usize = 8 + std::mem::size_of::<RewardDistributor>() + 64;
#[account]
pub struct RewardDistributor {
    pub bump: u8,
    pub stake_pool: Pubkey,
    pub kind: u8,
    pub authority: Pubkey,
    pub reward_mint: Pubkey,
    pub reward_amount: u64,
    pub reward_duration_seconds: u128,
    pub rewards_issued: u128,
    pub max_supply: Option<u64>,
    pub default_multiplier: u64,
    pub multiplier_decimals: u8,
    pub max_reward_seconds_received: Option<u128>,
}


