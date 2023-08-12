mempool/mempool-shared-proto/build.rs
=====================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! Builds the proto files needed for the mempool-shared-proto crate.
fn main() {
    let proto_files_prost = ["src/proto/mempool_status.proto"];
    let includes = ["src/proto"];
    prost_build::compile_protos(&proto_files_prost, &includes).unwrap();
}


