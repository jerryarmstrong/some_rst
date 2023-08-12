language/move-analyzer/src/lib.rs
=================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

#[macro_use(sp)]
extern crate move_ir_types;

pub mod completion;
pub mod context;
pub mod diagnostics;
pub mod symbols;
pub mod utils;
pub mod vfs;


