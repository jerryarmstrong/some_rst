tests/ui/structs-enums/struct-rec/mutual-struct-recursion.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A<T> {
//~^ ERROR recursive types `A` and `B` have infinite size
    x: T,
    y: B<T>,
}

struct B<T> {
    z: A<T>
}

struct C<T> {
//~^ ERROR recursive types `C` and `D` have infinite size
    x: T,
    y: Option<Option<D<T>>>,
}

struct D<T> {
    z: Option<Option<C<T>>>,
}

fn main() {}


