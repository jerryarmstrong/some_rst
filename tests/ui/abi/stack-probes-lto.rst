tests/ui/abi/stack-probes-lto.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-arm
// ignore-aarch64
// ignore-mips
// ignore-mips64
// ignore-sparc
// ignore-sparc64
// ignore-wasm
// ignore-emscripten no processes
// ignore-sgx no processes
// ignore-musl FIXME #31506
// ignore-pretty
// ignore-fuchsia no exception handler registered for segfault
// compile-flags: -C lto
// no-prefer-dynamic

include!("stack-probes.rs");


