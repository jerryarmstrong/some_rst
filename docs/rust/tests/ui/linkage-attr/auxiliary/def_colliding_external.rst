tests/ui/linkage-attr/auxiliary/def_colliding_external.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(linkage)]
#![crate_type = "lib"]

extern "C" {
    #[linkage = "external"]
    pub static collision: *const i32;
}


