tests/assembly/nvptx-arch-target-cpu.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // assembly-output: ptx-linker
// compile-flags: --crate-type cdylib -C target-cpu=sm_50
// only-nvptx64
// ignore-nvptx64

#![no_std]

// aux-build: breakpoint-panic-handler.rs
extern crate breakpoint_panic_handler;

// Verify target arch override via `target-cpu`.
// CHECK: .target sm_50
// CHECK: .address_size 64


