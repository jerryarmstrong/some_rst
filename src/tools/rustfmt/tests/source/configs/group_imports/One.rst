src/tools/rustfmt/tests/source/configs/group_imports/One.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-group_imports: One
use chrono::Utc;
use super::update::convert_publish_payload;

use juniper::{FieldError, FieldResult};
use uuid::Uuid;
use alloc::alloc::Layout;

use std::sync::Arc;

use broker::database::PooledConnection;

use super::schema::{Context, Payload};
use core::f32;
use crate::models::Event;


