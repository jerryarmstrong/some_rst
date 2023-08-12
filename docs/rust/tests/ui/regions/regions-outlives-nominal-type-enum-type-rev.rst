tests/ui/regions/regions-outlives-nominal-type-enum-type-rev.rs
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

mod variant_struct_type {
    struct Foo<T> {
        x: fn(T)
    }
    enum Bar<'a,'b> {
        V(&'a Foo<&'b i32>)
    }
}

fn main() { }


