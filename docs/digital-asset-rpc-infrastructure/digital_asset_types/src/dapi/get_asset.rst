digital_asset_types/src/dapi/get_asset.rs
=========================================

Last edited: 2023-07-27 22:02:16

Contents:

.. code-block:: rs

    use sea_orm::{DatabaseConnection, DbErr};

use crate::{dao::scopes, rpc::Asset};

use super::common::asset_to_rpc;

pub async fn get_asset(db: &DatabaseConnection, id: Vec<u8>) -> Result<Asset, DbErr> {
    let asset = scopes::asset::get_by_id(db, id, false).await?;
    asset_to_rpc(asset)
}


