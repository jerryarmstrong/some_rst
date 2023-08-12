tests/ui/consts/const-cast-ptr-int.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_upper_case_globals)]

use std::ptr;

struct TestStruct {
    x: *const u8
}

unsafe impl Sync for TestStruct {}

static a: TestStruct = TestStruct{x: 0 as *const u8};

pub fn main() {
    assert_eq!(a.x, ptr::null());
}


