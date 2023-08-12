src/tools/rustfmt/tests/target/configs/group_imports/StdExternalCrate-non_consecutive.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-group_imports: StdExternalCrate
use alloc::alloc::Layout;

use chrono::Utc;
use juniper::{FieldError, FieldResult};
use uuid::Uuid;

use super::update::convert_publish_payload;

extern crate uuid;

use core::f32;
use std::sync::Arc;

use broker::database::PooledConnection;

use super::schema::{Context, Payload};
use crate::models::Event;


