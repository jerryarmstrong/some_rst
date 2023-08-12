src/token.rs
============

Last edited: 2021-09-02 06:22:54

Contents:

.. code-block:: rs

    use {
    serde::{Deserialize, Serialize},
    solana_sdk::{clock::Slot, pubkey::Pubkey, signature::Signature},
};

#[derive(Clone, Debug, Default, Deserialize, Serialize)]
pub struct DelegateTransfer {
    pub slot: Slot,
    pub transaction_id: Signature,
    pub signer: Pubkey,
    pub amount: String,
    pub original_ix: String,
}

#[derive(Clone, Debug, Default, Deserialize, Serialize)]
pub struct DelegateBurn {
    pub slot: Slot,
    pub transaction_id: Signature,
    pub signer: Pubkey,
    pub amount: String,
    pub original_ix: String,
}

#[derive(Clone, Debug, Default, Deserialize, Serialize)]
pub struct OwnerChange {
    pub slot: Slot,
    pub transaction_id: Signature,
    pub signer: Pubkey,
    pub new_owner: Pubkey,
    pub original_ix: String,
}

#[derive(Clone, Debug, Default, Deserialize, Serialize)]
pub struct DelegateChange {
    pub slot: Slot,
    pub transaction_id: Signature,
    pub signer: Pubkey,
    pub new_delegate: Pubkey,
    pub original_ix: String,
}

#[derive(Clone, Debug, Default, Deserialize, Serialize)]
pub struct TokenAccountEntry {
    pub current_owner: Pubkey,
    pub mint: Pubkey,
    // intra slot tx order can't be guranteed.... so there is no perfect way to precisely track the
    // latest delegate_address, so we need to collect them all and detect possible attempts later
    pub all_delegate_addresses: std::collections::BTreeSet<Pubkey>,
    pub total_tx_count: usize,
    pub scanned_tx_count: usize,
    pub scanned_spl_token_ix_count: usize,
    pub failed_tx_count: usize,
    pub possible_delegate_transfers: Vec<DelegateTransfer>,
    pub possible_delegate_burns: Vec<DelegateBurn>,
    pub owner_changes: Vec<OwnerChange>,
    pub delegate_changes: Vec<DelegateChange>,
}

impl TokenAccountEntry {
    pub fn new(current_owner: Pubkey, mint: Pubkey) -> Self {
        Self {
            current_owner,
            mint,
            ..Self::default()
        }
    }
    // implement logic here to match any recognized delegate_address against delegate_transfers and
    // delegate_burns
}


