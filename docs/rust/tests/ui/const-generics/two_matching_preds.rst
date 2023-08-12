tests/ui/const-generics/two_matching_preds.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

fn foo<const N: usize>()
where
    [(); N + 1]:,
    [(); N + 1]:,
{
    bar::<N>();
}

fn bar<const N: usize>()
where
    [(); N + 1]:,
{
}

fn main() {}


