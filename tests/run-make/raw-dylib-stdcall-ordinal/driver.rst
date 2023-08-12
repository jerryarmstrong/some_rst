tests/run-make/raw-dylib-stdcall-ordinal/driver.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate raw_dylib_test;

fn main() {
    raw_dylib_test::library_function();
}


