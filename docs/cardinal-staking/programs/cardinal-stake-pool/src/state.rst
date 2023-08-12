programs/cardinal-stake-pool/src/state.rs
=========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: rs

    use crate::errors::ErrorCode;
use anchor_lang::prelude::*;
use solana_program::pubkey;
use std::str::FromStr;

// The keypair that has the ability to init the stake pool and reward distributor.
pub const INIT_AUTHORITY: Pubkey = pubkey!("EcxjN4mea6Ah9WSqZhLtSJJCZcxY73Vaz6UVHFZZ5Ttz");

pub const STAKE_ENTRY_PREFIX: &str = "stake-entry";
pub const STAKE_ENTRY_SIZE: usize = 8 + std::mem::size_of::<StakeEntry>() + 8;

pub const STAKE_POOL_PREFIX: &str = "stake-pool";
// 5 Pubkeys for creators and collections
pub const STAKE_POOL_SIZE: usize = 8 + 1 + 8 + 1 + 32 + 32 * 5 + 256;

pub const IDENTIFIER_PREFIX: &str = "identifier";
pub const IDENTIFIER_SIZE: usize = 8 + std::mem::size_of::<Identifier>() + 8;

pub const STAKE_AUTHORIZATION_PREFIX: &str = "stake-authorization";
pub const STAKE_AUTHORIZATION_SIZE: usize = 8 + std::mem::size_of::<StakeAuthorizationRecord>() + 8;

pub const GROUP_ENTRY_PREFIX: &str = "group-entry";
pub const GROUP_ENTRY_DEFAULT_SIZE: usize = 8 // Anchor discriminator/sighash
 + 1 // bump
 + 32 // group_id
 + 32 // authority
 + 4 + 32 // stake_entries (1 pubkeys)
 + 8 // changed_at
 + 4 // group_cooldown_seconds
 + 4 // group_stake_seconds
 + 8 // group_cooldown_start_seconds
 + 8; // padding

#[derive(Clone, Debug, PartialEq, Eq, AnchorSerialize, AnchorDeserialize)]
#[repr(u8)]
pub enum StakeEntryKind {
    Permissionless = 0, // original
    Permissioned = 1,   // someone else called update_total_stake_seconds indicating claim_reward must check signer so this is a permissioned claim_rewards
}

#[account]
pub struct GroupStakeEntry {
    pub bump: u8,
    pub group_id: Pubkey,
    pub authority: Pubkey,
    pub stake_entries: Vec<Pubkey>,
    pub changed_at: i64,
    pub group_cooldown_seconds: u32,
    pub group_stake_seconds: u32,
    pub group_cooldown_start_seconds: Option<i64>,
}

#[account]
pub struct StakeEntry {
    pub bump: u8,
    pub pool: Pubkey,
    pub amount: u64,
    pub original_mint: Pubkey,
    pub original_mint_claimed: bool,
    pub last_staker: Pubkey,
    pub last_staked_at: i64,
    pub total_stake_seconds: u128,
    pub stake_mint_claimed: bool,
    pub kind: u8,
    pub stake_mint: Option<Pubkey>,
    pub cooldown_start_seconds: Option<i64>,
    pub last_updated_at: Option<i64>,
    pub grouped: Option<bool>,
}

#[account]
pub struct StakePool {
    pub bump: u8,
    pub identifier: u64,
    pub authority: Pubkey,
    pub requires_creators: Vec<Pubkey>,
    pub requires_collections: Vec<Pubkey>,
    pub requires_authorization: bool,
    pub overlay_text: String,
    pub image_uri: String,
    pub reset_on_stake: bool,
    pub total_staked: u32,
    pub cooldown_seconds: Option<u32>,
    pub min_stake_seconds: Option<u32>,
    pub end_date: Option<i64>,
    pub double_or_reset_enabled: Option<bool>,
}

pub fn assert_stake_boost_payment_manager(pubkey: &Pubkey) -> Result<()> {
    if pubkey.to_string() != Pubkey::from_str("CuEDMUqgkGTVcAaqEDHuVR848XN38MPsD11JrkxcGD6a").unwrap().to_string() {
        return Err(error!(ErrorCode::InvalidPaymentManager));
    }
    Ok(())
}

pub const STAKE_BOOSTER_PREFIX: &str = "stake-booster";
pub const STAKE_BOOSTER_SIZE: usize = 8 + std::mem::size_of::<StakeBooster>() + 64;

#[account]
pub struct StakeBooster {
    pub bump: u8,
    pub stake_pool: Pubkey,
    pub identifier: u64,
    pub payment_amount: u64,
    pub payment_mint: Pubkey,
    pub payment_manager: Pubkey,
    pub payment_recipient: Pubkey,
    pub boost_seconds: u128,
    pub start_time_seconds: i64,
}

#[account]
pub struct StakeAuthorizationRecord {
    pub bump: u8,
    pub pool: Pubkey,
    pub mint: Pubkey,
}

#[account]
pub struct Identifier {
    pub bump: u8,
    pub count: u64,
}

pub fn get_stake_seed(supply: u64, user: Pubkey) -> Pubkey {
    if supply > 1 {
        user
    } else {
        Pubkey::default()
    }
}

pub fn stake_entry_fill_zeros(stake_entry: &mut Account<StakeEntry>) -> Result<()> {
    let stake_entry_account = stake_entry.to_account_info();
    let mut stake_entry_data = stake_entry_account.data.borrow_mut();
    let len = stake_entry_data.len();
    stake_entry_data[stake_entry.try_to_vec()?.len()..len].iter_mut().for_each(|d| *d = 0);
    Ok(())
}


