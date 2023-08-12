tests/run-make-fulldeps/lto-dylib-dep/main.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate a_dylib;

fn main() {
    a_dylib::foo();
}


