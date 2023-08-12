tests/ui/lto/auxiliary/msvc-imp-present.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
// compile-flags: -Z thinlto -C codegen-units=8 -C prefer-dynamic

#![crate_type = "rlib"]
#![crate_type = "dylib"]

pub static A: u32 = 43;

pub mod a {
    pub static A: u32 = 43;
}


