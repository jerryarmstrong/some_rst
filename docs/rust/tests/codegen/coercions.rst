tests/codegen/coercions.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C no-prepopulate-passes

#![crate_type = "lib"]

static X: i32 = 5;

// CHECK-LABEL: @raw_ptr_to_raw_ptr_noop
// CHECK-NOT: alloca
#[no_mangle]
pub fn raw_ptr_to_raw_ptr_noop() -> *const i32{
    &X as *const i32
}

// CHECK-LABEL: @reference_to_raw_ptr_noop
// CHECK-NOT: alloca
#[no_mangle]
pub fn reference_to_raw_ptr_noop() -> *const i32 {
    &X
}


