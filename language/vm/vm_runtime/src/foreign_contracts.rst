language/vm/vm_runtime/src/foreign_contracts.rs
===============================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! This file contains models of the vm crate's dependencies for use with MIRAI.

pub mod types {
    pub mod transaction {
        pub const MAX_TRANSACTION_SIZE_IN_BYTES: usize = 4096;
    }
}


