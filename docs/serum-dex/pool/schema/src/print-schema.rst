pool/schema/src/print-schema.rs
===============================

Last edited: 2021-05-20 03:21:28

Contents:

.. code-block:: rs

    use borsh::schema::{BorshSchema, BorshSchemaContainer};
use borsh::BorshSerialize;

use schema::PoolRequest;
use schema::PoolState;

mod schema;

fn main() -> std::io::Result<()> {
    let mut schema: BorshSchemaContainer = PoolState::schema_container();
    PoolRequest::add_definitions_recursively(&mut schema.definitions);
    schema.serialize(&mut std::io::stdout())
}


