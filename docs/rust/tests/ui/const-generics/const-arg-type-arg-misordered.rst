tests/ui/const-generics/const-arg-type-arg-misordered.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type Array<T, const N: usize> = [T; N];

fn foo<const N: usize>() -> Array<N, ()> {
    //~^ ERROR constant provided when a type was expected
    unimplemented!()
}

fn main() {}


