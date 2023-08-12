tests/codegen/noalias-flag.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O -Zmutable-noalias=no

#![crate_type = "lib"]

// `-Zmutable-noalias=no` should disable noalias on mut refs...

// CHECK-LABEL: @test_mut_ref(
// CHECK-NOT: noalias
// CHECK-SAME: %x
#[no_mangle]
pub fn test_mut_ref(x: &mut i32) -> &mut i32 {
    x
}

// ...but not on shared refs

// CHECK-LABEL: @test_ref(
// CHECK-SAME: noalias
// CHECK-SAME: %x
#[no_mangle]
pub fn test_ref(x: &i32) -> &i32 {
    x
}


