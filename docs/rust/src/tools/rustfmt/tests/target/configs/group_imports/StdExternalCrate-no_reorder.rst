src/tools/rustfmt/tests/target/configs/group_imports/StdExternalCrate-no_reorder.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-group_imports: StdExternalCrate
// rustfmt-reorder_imports: false

use alloc::alloc::Layout;
use std::sync::Arc;
use core::f32;

use chrono::Utc;
use juniper::{FieldError, FieldResult};
use uuid::Uuid;
use broker::database::PooledConnection;

use super::update::convert_publish_payload;
use super::schema::{Context, Payload};
use crate::models::Event;


