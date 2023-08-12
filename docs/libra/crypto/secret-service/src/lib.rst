crypto/secret-service/src/lib.rs
================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

#![deny(missing_docs)]
//! A secret service providing cryptographic operations on secret keys, will be used in future
//! releases.
pub mod crypto_wrappers;
pub mod proto;
pub mod secret_service_client;

pub mod secret_service_node;
pub mod secret_service_server;


