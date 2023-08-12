tests/ui/const-generics/generic_const_exprs/abstract-consts-as-cast-5.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

fn foo<const N: u8>(a: [(); N as usize]) {
    bar::<{ N as usize as usize }>();
    //~^ error: unconstrained generic constant
}

fn bar<const N: usize>() {}

fn main() {}


