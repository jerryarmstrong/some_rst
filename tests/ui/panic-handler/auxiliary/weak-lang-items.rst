tests/ui/panic-handler/auxiliary/weak-lang-items.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

// This aux-file will require the eh_personality function to be codegen'd, but
// it hasn't been defined just yet. Make sure we don't explode.

#![no_std]
#![crate_type = "rlib"]

struct A;

impl core::ops::Drop for A {
    fn drop(&mut self) {}
}

pub fn foo() {
    let _a = A;
    panic!("wut");
}

mod std {
    pub use core::{option, fmt};
}


