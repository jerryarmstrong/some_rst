bucket_map/src/bucket_item.rs
=============================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: rs

    use {crate::RefCount, solana_sdk::pubkey::Pubkey};

#[derive(Debug, Default, Clone)]
pub struct BucketItem<T> {
    pub pubkey: Pubkey,
    pub ref_count: RefCount,
    pub slot_list: Vec<T>,
}


