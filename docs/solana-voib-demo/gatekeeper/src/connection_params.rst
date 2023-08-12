gatekeeper/src/connection_params.rs
===================================

Last edited: 2019-08-29 17:32:23

Contents:

.. code-block:: rs

    use serde_derive::Deserialize;
use solana_sdk::pubkey::Pubkey;

#[derive(Deserialize)]
pub struct NewConnParams {
    pub contract_pubkey: Pubkey,
    pub destination: String,
    pub fee_interval: u16,
}


