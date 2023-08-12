tests/ui/const-generics/fn_with_two_const_inputs.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_const_exprs)]
#![allow(incomplete_features)]

const fn both(_: usize, b: usize) -> usize {
    b
}

fn foo<const N: usize, const M: usize>() -> [(); N + 2]
where
    [(); both(N + 1, M + 1)]:,
{
    bar()
    //~^ ERROR: unconstrained generic constant
}

fn bar<const N: usize>() -> [(); N]
where
    [(); N + 1]:,
{
    [(); N]
}

fn main() {}


