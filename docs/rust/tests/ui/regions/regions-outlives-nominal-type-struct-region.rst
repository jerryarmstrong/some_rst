tests/ui/regions/regions-outlives-nominal-type-struct-region.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a nominal type (like `Foo<'a>`) outlives `'b` if its
// arguments (like `'a`) outlive `'b`.
//
// Rule OutlivesNominalType from RFC 1214.

// check-pass

#![feature(rustc_attrs)]
#![allow(dead_code)]

mod variant_struct_region {
    struct Foo<'a> {
        x: &'a i32,
    }
    struct Bar<'a,'b> {
        f: &'a Foo<'b>
    }
}

fn main() { }


