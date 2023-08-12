tests/codegen/option-nonzero-eq.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O -Zmerge-functions=disabled

#![crate_type = "lib"]

extern crate core;
use core::num::{NonZeroU32, NonZeroI64};
use core::ptr::NonNull;

// CHECK-lABEL: @non_zero_eq
#[no_mangle]
pub fn non_zero_eq(l: Option<NonZeroU32>, r: Option<NonZeroU32>) -> bool {
    // CHECK: start:
    // CHECK-NEXT: icmp eq i32
    // CHECK-NEXT: ret i1
    l == r
}

// CHECK-lABEL: @non_zero_signed_eq
#[no_mangle]
pub fn non_zero_signed_eq(l: Option<NonZeroI64>, r: Option<NonZeroI64>) -> bool {
    // CHECK: start:
    // CHECK-NEXT: icmp eq i64
    // CHECK-NEXT: ret i1
    l == r
}

// CHECK-lABEL: @non_null_eq
#[no_mangle]
pub fn non_null_eq(l: Option<NonNull<u8>>, r: Option<NonNull<u8>>) -> bool {
    // CHECK: start:
    // CHECK-NEXT: icmp eq {{(i8\*|ptr)}}
    // CHECK-NEXT: ret i1
    l == r
}


