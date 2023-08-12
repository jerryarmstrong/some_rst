tests/ui/const-generics/parent_generics_of_encoding_impl_trait.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:generics_of_parent_impl_trait.rs
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

extern crate generics_of_parent_impl_trait;

fn main() {
    // check for `impl Trait<{ const }>` which has a parent of a `DefKind::TyParam`
    generics_of_parent_impl_trait::foo([()]);
    //~^ error: type annotations needed
}


