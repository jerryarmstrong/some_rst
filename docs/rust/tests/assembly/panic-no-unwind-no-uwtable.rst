tests/assembly/panic-no-unwind-no-uwtable.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // assembly-output: emit-asm
// only-x86_64-unknown-linux-gnu
// compile-flags: -C panic=unwind -C force-unwind-tables=n -O

#![crate_type = "lib"]

// CHECK-NOT: .cfi_startproc
pub fn foo() {}


