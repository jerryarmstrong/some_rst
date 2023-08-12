tests/codegen/sbf-alu32.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-sbf
#![crate_type = "lib"]
#![feature(sbf_target_feature)]
#![no_std]

#[no_mangle]
#[target_feature(enable = "alu32")]
// CHECK: define i8 @foo(i8 returned %arg) unnamed_addr #0 {
pub unsafe fn foo(arg: u8) -> u8 {
    arg
}


