tests/ui/generics/generic-type-less-params-with-defaults.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::marker;

struct Heap;

struct Vec<T, A = Heap>(
    marker::PhantomData<(T,A)>);

fn main() {
    let _: Vec;
    //~^ ERROR missing generics for struct `Vec`
}


