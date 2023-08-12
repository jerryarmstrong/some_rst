migration/src/main.rs
=====================

Last edited: 2023-07-27 22:02:16

Contents:

.. code-block:: rs

    use sea_orm_migration::prelude::*;

#[async_std::main]
async fn main() {
    cli::run_cli(migration::Migrator).await;
}


