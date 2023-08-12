tests/codegen/noalias-box.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O

#![crate_type = "lib"]

// CHECK-LABEL: @box_should_have_noalias_by_default(
// CHECK: noalias
#[no_mangle]
pub fn box_should_have_noalias_by_default(_b: Box<u8>) {}


