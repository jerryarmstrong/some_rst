programs/wbtc/src/instructions/mod.rs
=====================================

Last edited: 2023-06-16 20:26:13

Contents:

.. code-block:: rs

    pub mod approve_mint_request;
pub mod approve_redeem_request;
pub mod cancel_mint_request;
pub mod claim_authority;
pub mod create_merchant;
pub mod create_mint_request;
pub mod create_redeem_request;
pub mod delete_merchant;
pub mod initialize;
pub mod reject_mint_request;
pub mod set_authority;
pub mod set_custodian;
pub mod set_custodian_btc_address;
pub mod set_merchant_authority;
pub mod set_merchant_btc_address;
pub mod toggle_functionality_enabled;
pub mod toggle_merchant_enabled;

pub use approve_mint_request::*;
pub use approve_redeem_request::*;
pub use cancel_mint_request::*;
pub use claim_authority::*;
pub use create_merchant::*;
pub use create_mint_request::*;
pub use create_redeem_request::*;
pub use delete_merchant::*;
pub use initialize::*;
pub use reject_mint_request::*;
pub use set_authority::*;
pub use set_custodian::*;
pub use set_custodian_btc_address::*;
pub use set_merchant_authority::*;
pub use set_merchant_btc_address::*;
pub use toggle_functionality_enabled::*;
pub use toggle_merchant_enabled::*;


