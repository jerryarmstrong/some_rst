tests/assembly/nvptx-arch-emit-asm.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // assembly-output: emit-asm
// compile-flags: --crate-type rlib
// only-nvptx64
// ignore-nvptx64

#![no_std]

// Verify default arch without ptx-linker involved.
// CHECK: .target sm_30
// CHECK: .address_size 64


