nft_ingester/src/program_transformers/bubblegum/decompress.rs
=============================================================

Last edited: 2023-07-27 22:02:16

Contents:

.. code-block:: rs

    use crate::{
    error::IngesterError,
    program_transformers::bubblegum::{
        upsert_asset_with_compression_info, upsert_asset_with_leaf_info,
    },
};
use blockbuster::{instruction::InstructionBundle, programs::bubblegum::BubblegumInstruction};
use sea_orm::{ConnectionTrait, TransactionTrait};

pub async fn decompress<'c, T>(
    _parsing_result: &BubblegumInstruction,
    bundle: &InstructionBundle<'c>,
    txn: &'c T,
) -> Result<(), IngesterError>
where
    T: ConnectionTrait + TransactionTrait,
{
    let id_bytes = bundle.keys.get(3).unwrap().0.as_slice();

    // Partial update of asset table with just leaf.
    upsert_asset_with_leaf_info(txn, id_bytes.to_vec(), None, None, true).await?;

    upsert_asset_with_compression_info(
        txn,
        id_bytes.to_vec(),
        false,
        false,
        1,
        Some(id_bytes.to_vec()),
        true,
    )
    .await
}


