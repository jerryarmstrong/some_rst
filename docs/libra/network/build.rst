network/build.rs
================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

/// Builds the proto files needed for the network crate.
fn main() {
    let proto_files = [
        "src/proto/consensus.proto",
        "src/proto/mempool.proto",
        "src/proto/network.proto",
        "src/proto/state_synchronizer.proto",
    ];

    let includes = [
        "../types/src/proto",
        "src/proto",
        "../admission_control/admission_control_proto/src/proto",
    ];

    prost_build::compile_protos(&proto_files, &includes).unwrap();
}


