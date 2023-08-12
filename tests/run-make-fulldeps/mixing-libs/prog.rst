tests/run-make-fulldeps/mixing-libs/prog.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate dylib;
extern crate rlib;

fn main() {
    dylib::dylib();
    rlib::rlib();
}


