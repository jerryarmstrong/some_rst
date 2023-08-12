tests/ui/const-generics/occurs-check/bind-param.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

// This test does not use any "unevaluated" consts, so it should compile just fine.

fn bind<const N: usize>(value: [u8; N]) -> [u8; N] {
    todo!()
}

fn sink(_: [u8; 5]) {}

fn main() {
    let mut arr = Default::default();
    arr = bind(arr);
    sink(arr);
}


