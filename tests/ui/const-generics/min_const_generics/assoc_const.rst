tests/ui/const-generics/min_const_generics/assoc_const.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
struct Foo<const N: usize>;

impl<const N: usize> Foo<N> {
    const VALUE: usize = N * 2;
}

trait Bar {
    const ASSOC: usize;
}

impl<const N: usize> Bar for Foo<N> {
    const ASSOC: usize = N * 3;
}

fn main() {}


