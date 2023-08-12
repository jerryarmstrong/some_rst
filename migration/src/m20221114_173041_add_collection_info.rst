migration/src/m20221114_173041_add_collection_info.rs
=====================================================

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
                    .add_column(ColumnDef::new(Alias::new("collection")).binary())
                    .to_owned(),
            )
            .await?;

        manager
            .alter_table(
                sea_query::Table::alter()
                    .table(asset::Entity)
                    .add_column(
                        ColumnDef::new(Alias::new("collection_verified"))
                            .boolean()
                            .default(false)
                            .not_null(),
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
                    .drop_column(Alias::new("collection"))
                    .to_owned(),
            )
            .await?;
        manager
            .alter_table(
                sea_query::Table::alter()
                    .table(asset::Entity)
                    .drop_column(Alias::new("collection_verified"))
                    .to_owned(),
            )
            .await?;

        Ok(())
    }
}


