tests/ui/rfc-2093-infer-outlives/regions-outlives-nominal-type-region.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a nominal type (like `Foo<'a>`) outlives `'b` if its
// arguments (like `'a`) outlive `'b`.
//
// Rule OutlivesNominalType from RFC 1214.


#![allow(dead_code)]

mod variant_struct_region {
    struct Foo<'a> {
        x: &'a i32,
    }
    trait Trait<'a, 'b> {
        type Out;
    }
    impl<'a, 'b> Trait<'a, 'b> for usize {
        type Out = &'a Foo<'b>; //~ ERROR reference has a longer lifetime
    }
}


fn main() { }


