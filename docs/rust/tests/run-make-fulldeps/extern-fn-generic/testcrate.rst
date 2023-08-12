tests/run-make-fulldeps/extern-fn-generic/testcrate.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

#[repr(C)]
pub struct TestStruct<T> {
    pub x: u8,
    pub y: T,
}

pub extern "C" fn foo<T>(ts: TestStruct<T>) -> T {
    ts.y
}

#[link(name = "test", kind = "static")]
extern "C" {
    pub fn call(c: extern "C" fn(TestStruct<i32>) -> i32) -> i32;
}


