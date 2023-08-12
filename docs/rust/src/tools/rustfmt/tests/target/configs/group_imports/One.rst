src/tools/rustfmt/tests/target/configs/group_imports/One.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-group_imports: One
use super::schema::{Context, Payload};
use super::update::convert_publish_payload;
use crate::models::Event;
use alloc::alloc::Layout;
use broker::database::PooledConnection;
use chrono::Utc;
use core::f32;
use juniper::{FieldError, FieldResult};
use std::sync::Arc;
use uuid::Uuid;


