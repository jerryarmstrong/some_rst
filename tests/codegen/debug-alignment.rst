tests/codegen/debug-alignment.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verifies that DWARF alignment is specified properly.
//
// compile-flags: -C debuginfo=2
#![crate_type = "lib"]

// CHECK: !DIGlobalVariable
// CHECK: align: 32
pub static A: u32 = 1;


