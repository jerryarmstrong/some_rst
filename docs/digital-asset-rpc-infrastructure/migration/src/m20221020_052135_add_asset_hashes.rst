migration/src/m20221020_052135_add_asset_hashes.rs
==================================================

Last edited: 2023-07-27 22:02:16

Contents:

.. code-block:: rs

    use digital_asset_types::dao::asset;
use sea_orm_migration::prelude::*;

#[derive(DeriveMigrationName)]
pub struct Migration;

#[async_trait::async_trait]
impl MigrationTrait for Migration {
    async fn up(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        manager
            .alter_table(
                sea_query::Table::alter()
                    .table(asset::Entity)
                    .add_column(
                        ColumnDef::new(Alias::new("data_hash"))
                            .string()
                            .char_len(50),
                    )
                    .to_owned(),
            )
            .await?;
        manager
            .alter_table(
                sea_query::Table::alter()
                    .table(asset::Entity)
                    .add_column(
                        ColumnDef::new(Alias::new("creator_hash"))
                            .string()
                            .char_len(50),
                    )
                    .to_owned(),
            )
            .await?;
        Ok(())
    }

    async fn down(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        manager
            .alter_table(
                sea_query::Table::alter()
                    .table(asset::Entity)
                    .drop_column(Alias::new("data_hash"))
                    .to_owned(),
            )
            .await?;
        manager
            .alter_table(
                sea_query::Table::alter()
                    .table(asset::Entity)
                    .drop_column(Alias::new("creator_hash"))
                    .to_owned(),
            )
            .await?;
        Ok(())
    }
}


