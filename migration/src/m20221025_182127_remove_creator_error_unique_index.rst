migration/src/m20221025_182127_remove_creator_error_unique_index.rs
===================================================================

Last edited: 2023-07-27 22:02:16

Contents:

.. code-block:: rs

    use digital_asset_types::dao::asset_creators;
use sea_orm_migration::prelude::*;

#[derive(DeriveMigrationName)]
pub struct Migration;

#[async_trait::async_trait]
impl MigrationTrait for Migration {
    async fn up(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        // Replace the sample below with your own migration scripts
        manager
            .drop_index(
                sea_query::Index::drop()
                    .name("asset_creators_asset_id")
                    .table(asset_creators::Entity)
                    .to_owned(),
            )
            .await?;
        Ok(())
    }

    async fn down(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        println!("Down migration not implemented");
        Ok(())
    }
}


