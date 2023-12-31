tests/ui/variance/variance-associated-types.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the variance computation considers types/regions that
// appear in projections to be invariant.

#![feature(rustc_attrs)]

trait Trait<'a> {
    type Type;

    fn method(&'a self) { }
}

#[rustc_variance]
struct Foo<'a, T : Trait<'a>> { //~ ERROR [-, +]
    field: (T, &'a ())
}

#[rustc_variance]
struct Bar<'a, T : Trait<'a>> { //~ ERROR [o, o]
    field: <T as Trait<'a>>::Type
}

fn main() { }


