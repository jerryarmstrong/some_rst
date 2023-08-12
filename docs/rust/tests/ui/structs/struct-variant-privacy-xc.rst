tests/ui/structs/struct-variant-privacy-xc.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:struct_variant_privacy.rs
extern crate struct_variant_privacy;

fn f(b: struct_variant_privacy::Bar) {
    //~^ ERROR enum `Bar` is private
    match b {
        struct_variant_privacy::Bar::Baz { a: _a } => {} //~ ERROR enum `Bar` is private
    }
}

fn main() {}


