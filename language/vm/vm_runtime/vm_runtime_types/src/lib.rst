language/vm/vm_runtime/vm_runtime_types/src/lib.rs
==================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! Types and data used by the VM runtime

#[macro_use]
extern crate lazy_static;

#[cfg(any(test, feature = "testing"))]
mod proptest_types;

pub mod loaded_data;
pub mod native_functions;
pub mod native_structs;
pub mod type_context;
pub mod value;


