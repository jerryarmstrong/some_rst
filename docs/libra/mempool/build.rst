mempool/build.rs
================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

fn main() {
    let protos = ["src/proto/mempool.proto"];

    let includes = [
        "../types/src/proto",
        "src/proto",
        "mempool-shared-proto/src/proto/",
    ];

    grpcio_compiler::prost_codegen::compile_protos(
        &protos,
        &includes,
        &std::env::var("OUT_DIR").unwrap(),
    )
    .unwrap();
}


