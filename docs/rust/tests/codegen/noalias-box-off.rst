tests/codegen/noalias-box-off.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O -Z box-noalias=no

#![crate_type = "lib"]

// CHECK-LABEL: @box_should_not_have_noalias_if_disabled(
// CHECK-NOT: noalias
#[no_mangle]
pub fn box_should_not_have_noalias_if_disabled(_b: Box<u8>) {}


