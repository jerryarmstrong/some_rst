tests/ui/lint/issue-31924-non-snake-ffi.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(non_snake_case)]

#[no_mangle]
pub extern "C" fn SparklingGenerationForeignFunctionInterface() {} // OK

pub struct Foo;

impl Foo {
    #[no_mangle]
    pub extern "C" fn SparklingGenerationForeignFunctionInterface() {} // OK
}

fn main() {}


