tests/codegen/array-clone.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O

#![crate_type = "lib"]

// CHECK-LABEL: @array_clone
#[no_mangle]
pub fn array_clone(a: &[u8; 2]) -> [u8; 2] {
    // CHECK-NOT: getelementptr
    // CHECK-NOT: load i8
    // CHECK-NOT: zext
    // CHECK-NOT: shl
    // CHECK: load i16
    // CHECK-NEXT: ret i16
    a.clone()
}


