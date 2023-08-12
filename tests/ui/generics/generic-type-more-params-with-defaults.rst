tests/ui/generics/generic-type-more-params-with-defaults.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::marker;

struct Heap;

struct Vec<T, A = Heap>(
    marker::PhantomData<(T,A)>);

fn main() {
    let _: Vec<isize, Heap, bool>;
    //~^ ERROR this struct takes at most 2 generic arguments but 3 generic arguments
}


