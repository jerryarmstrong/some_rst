migration/src/m20221104_094327_add_backfiller_failed.rs
=======================================================

Last edited: 2023-07-27 22:02:16

Contents:

.. code-block:: rs

    use digital_asset_types::dao::backfill_items;
use sea_orm_migration::prelude::*;

#[derive(DeriveMigrationName)]
pub struct Migration;

#[async_trait::async_trait]
impl MigrationTrait for Migration {
    async fn up(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        // Replace the sample below with your own migration scripts
        manager
            .alter_table(
                Table::alter()
                    .table(backfill_items::Entity)
                    .add_column(
                        ColumnDef::new(Alias::new("failed"))
                            .boolean()
                            .not_null()
                            .default(false),
                    )
                    .to_owned(),
            )
            .await
    }

    async fn down(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        // Replace the sample below with your own migration scripts
        manager
            .alter_table(
                Table::alter()
                    .table(backfill_items::Entity)
                    .drop_column(Alias::new("failed"))
                    .to_owned(),
            )
            .await
    }
}


