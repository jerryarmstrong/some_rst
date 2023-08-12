src/tools/rustfmt/tests/target/configs/group_imports/StdExternalCrate-merge_imports.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-group_imports: StdExternalCrate
// rustfmt-imports_granularity: Crate
use alloc::{alloc::Layout, vec::Vec};
use core::f32;
use std::sync::Arc;

use broker::database::PooledConnection;
use chrono::Utc;
use juniper::{FieldError, FieldResult};
use uuid::Uuid;

use super::{
    schema::{Context, Payload},
    update::convert_publish_payload,
};
use crate::models::Event;


