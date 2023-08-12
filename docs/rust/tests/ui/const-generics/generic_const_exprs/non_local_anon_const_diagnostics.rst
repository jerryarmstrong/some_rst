tests/ui/const-generics/generic_const_exprs/non_local_anon_const_diagnostics.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:anon_const_non_local.rs

#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

extern crate anon_const_non_local;

fn bar<const M: usize>()
where
    [(); M + 1]:,
{
    let _: anon_const_non_local::Foo<2> = anon_const_non_local::foo::<M>();
    //~^ ERROR: mismatched types
}

fn main() {}


