tests/run-make-fulldeps/mixing-libs/dylib.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "dylib"]
extern crate rlib;

pub fn dylib() { rlib::rlib() }


