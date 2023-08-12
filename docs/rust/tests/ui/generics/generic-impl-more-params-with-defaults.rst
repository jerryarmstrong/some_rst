tests/ui/generics/generic-impl-more-params-with-defaults.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::marker;

struct Heap;

struct Vec<T, A = Heap>(
    marker::PhantomData<(T,A)>);

impl<T, A> Vec<T, A> {
    fn new() -> Vec<T, A> {Vec(marker::PhantomData)}
}

fn main() {
    Vec::<isize, Heap, bool>::new();
    //~^ ERROR this struct takes at most 2 generic arguments but 3 generic arguments were supplied
}


