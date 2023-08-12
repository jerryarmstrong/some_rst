migration/src/m20230601_120101_add_pnft_enum_val.rs
===================================================

Last edited: 2023-07-27 22:02:16

Contents:

.. code-block:: rs

    use sea_orm_migration::{
    prelude::*,
    sea_orm::{ConnectionTrait, DatabaseBackend, Statement},
};

#[derive(DeriveMigrationName)]
pub struct Migration;

#[async_trait::async_trait]
impl MigrationTrait for Migration {
    async fn up(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        // Replace the sample below with your own migration scripts
        manager
            .get_connection()
            .execute(Statement::from_string(
                DatabaseBackend::Postgres,
                "ALTER TYPE specification_asset_class ADD VALUE IF NOT EXISTS 'PROGRAMMABLE_NFT';"
                    .to_string(),
            ))
            .await?;

        Ok(())
    }

    async fn down(&self, _manager: &SchemaManager) -> Result<(), DbErr> {
        // Replace the sample below with your own migration scripts
        Ok(())
    }
}


