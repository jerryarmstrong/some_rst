tests/incremental/const-generics/hash-tyvid-regression-1.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: cfail
#![feature(generic_const_exprs, adt_const_params)]
#![allow(incomplete_features)]
// regression test for #77650
fn c<T, const N: std::num::NonZeroUsize>()
where
    [T; N.get()]: Sized,
{
    use std::convert::TryFrom;
    <[T; N.get()]>::try_from(())
    //~^ error: the trait bound
    //~| error: the trait bound
    //~| error: mismatched types
}

fn main() {}


