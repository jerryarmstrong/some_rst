src/tools/rustfmt/tests/target/configs/group_imports/One-merge_imports.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-group_imports: One
// rustfmt-imports_granularity: Crate
use super::{
    schema::{Context, Payload},
    update::convert_publish_payload,
};
use crate::models::Event;
use alloc::{alloc::Layout, vec::Vec};
use broker::database::PooledConnection;
use chrono::Utc;
use core::f32;
use juniper::{FieldError, FieldResult};
use std::sync::Arc;
use uuid::Uuid;


