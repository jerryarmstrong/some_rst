tests/ui/const-generics/fn_with_two_same_const_inputs.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

const fn both(_: usize, b: usize) -> usize {
    b
}

fn foo<const N: usize>()
where
    [(); both(N + 1, N + 1)]:,
{
    bar::<N>();
}

fn bar<const N: usize>()
where
    [(); N + 1]:,
{
}

fn main() {}


