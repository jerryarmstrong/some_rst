tests/ui/const-generics/occurs-check/unify-n-nplusone.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

// This test would tries to unify `N` with `N + 1` which must fail the occurs check.

fn bind<const N: usize>(value: [u8; N]) -> [u8; N + 1] {
    todo!()
}

fn sink(_: [u8; 5]) {}

fn main() {
    let mut arr = Default::default();
    arr = bind(arr); //~ ERROR mismatched types
    sink(arr);
}


