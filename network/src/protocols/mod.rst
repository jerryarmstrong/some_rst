network/src/protocols/mod.rs
============================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! Protocols used by network module for external APIs and internal functionality
//!
//! Each protocol corresponds to a certain order of messages
pub mod direct_send;
pub mod rpc;

pub(crate) mod discovery;
pub(crate) mod health_checker;
pub(crate) mod identity;


