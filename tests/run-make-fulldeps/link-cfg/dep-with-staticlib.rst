tests/run-make-fulldeps/link-cfg/dep-with-staticlib.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(link_cfg)]
#![crate_type = "rlib"]

#[link(name = "return1", cfg(foo))]
#[link(name = "return3", kind = "static", cfg(bar))]
extern "C" {
    pub fn my_function() -> i32;
}


