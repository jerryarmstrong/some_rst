tests/codegen/issue-34947-pow-i32.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O

#![crate_type = "lib"]

// CHECK-LABEL: @issue_34947
#[no_mangle]
pub fn issue_34947(x: i32) -> i32 {
    // CHECK: mul
    // CHECK-NEXT: mul
    // CHECK-NEXT: mul
    // CHECK-NEXT: ret
    x.pow(5)
}


