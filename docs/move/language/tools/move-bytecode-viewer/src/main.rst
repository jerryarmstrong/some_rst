language/tools/move-bytecode-viewer/src/main.rs
===============================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

#![forbid(unsafe_code)]

use clap::Parser;
use move_bytecode_viewer::BytecodeViewerConfig;

fn main() {
    BytecodeViewerConfig::parse().start_viewer()
}


