blockbuster/src/programs/candy_machine/state.rs
===============================================

Last edited: 2023-06-27 20:46:29

Contents:

.. code-block:: rs

    /// These are copied over from mpl-candy-machine due to current Solana/Anchor version conflict
/// between that program and mpl-bubblegum, spl-account-compression, and spl-noop.
use borsh::{BorshDeserialize, BorshSerialize};
use solana_sdk::pubkey::Pubkey;

/// Candy machine state and config data.
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Default, Debug, Clone)]
pub struct CandyMachine {
    pub authority: Pubkey,
    pub wallet: Pubkey,
    pub token_mint: Option<Pubkey>,
    pub items_redeemed: u64,
    pub data: CandyMachineData,
    // there's a borsh vec u32 denoting how many actual lines of data there are currently (eventually equals items available)
    // There is actually lines and lines of data after this but we explicitly never want them deserialized.
    // here there is a borsh vec u32 indicating number of bytes in bitmask array.
    // here there is a number of bytes equal to ceil(max_number_of_lines/8) and it is a bit mask used to figure out when to increment borsh vec u32
}

/// Collection PDA account
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Default, Debug, Clone)]
pub struct CollectionPDA {
    pub mint: Pubkey,
    pub candy_machine: Pubkey,
}

/// Collection PDA account
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Default, Debug, Clone)]
pub struct FreezePDA {
    // duplicate key in order to find the candy machine without txn crawling
    pub candy_machine: Pubkey,   // 32
    pub allow_thaw: bool,        // 1
    pub frozen_count: u64,       // 8
    pub mint_start: Option<i64>, // 1 + 8
    pub freeze_time: i64,        // 8
    pub freeze_fee: u64,         // 8
}

/// Candy machine settings data.
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Default, Debug, Clone)]
pub struct CandyMachineData {
    pub uuid: String,
    pub price: u64,
    /// The symbol for the asset
    pub symbol: String,
    /// Royalty basis points that goes to creators in secondary sales (0-10000)
    pub seller_fee_basis_points: u16,
    pub max_supply: u64,
    pub is_mutable: bool,
    pub retain_authority: bool,
    pub go_live_date: Option<i64>,
    pub end_settings: Option<EndSettings>,
    pub creators: Vec<Creator>,
    pub hidden_settings: Option<HiddenSettings>,
    pub whitelist_mint_settings: Option<WhitelistMintSettings>,
    pub items_available: u64,
    /// If [`Some`] requires gateway tokens on mint
    pub gatekeeper: Option<GatekeeperConfig>,
}

/// Individual config line for storing NFT data pre-mint.
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub struct ConfigLine {
    pub name: String,
    /// URI pointing to JSON representing the asset
    pub uri: String,
}

#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub struct EndSettings {
    pub end_setting_type: EndSettingType,
    pub number: u64,
}

#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub enum EndSettingType {
    Date,
    Amount,
}

// Unfortunate duplication of token metadata so that IDL picks it up.
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub struct Creator {
    pub address: Pubkey,
    pub verified: bool,
    // In percentages, NOT basis points ;) Watch out!
    pub share: u8,
}

/// Hidden Settings for large mints used with offline data.
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub struct HiddenSettings {
    pub name: String,
    pub uri: String,
    pub hash: [u8; 32],
}

#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub struct WhitelistMintSettings {
    pub mode: WhitelistMintMode,
    pub mint: Pubkey,
    pub presale: bool,
    pub discount_price: Option<u64>,
}

#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Debug, Clone)]
pub enum WhitelistMintMode {
    // Only captcha uses the bytes, the others just need to have same length
    // for front end borsh to not crap itself
    // Holds the validation window
    BurnEveryTime,
    NeverBurn,
}

/// Configurations options for the gatekeeper.
#[derive(BorshSerialize, BorshDeserialize, PartialEq, Eq, Default, Debug, Clone)]
pub struct GatekeeperConfig {
    /// The network for the gateway token required
    pub gatekeeper_network: Pubkey,
    /// Whether or not the token should expire after minting.
    /// The gatekeeper network must support this if true.
    pub expire_on_use: bool,
}


