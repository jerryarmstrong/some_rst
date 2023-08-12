tests/codegen/no-assumes-on-casts.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

// compile-flags: -Cno-prepopulate-passes

// CHECK-LABEL: fna
#[no_mangle]
pub fn fna(a: i16) -> i32 {
    a as i32
// CHECK-NOT: assume
// CHECK: sext
}

// CHECK-LABEL: fnb
#[no_mangle]
pub fn fnb(a: u16) -> u32 {
    a as u32
// CHECK-NOT: assume
// CHECK: zext
}


