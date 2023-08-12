tests/ui/generic-associated-types/issue-102335-gat.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait T {
    type A: S<C<(), i32 = ()> = ()>;
    //~^ ERROR associated type bindings are not allowed here
}

trait Q {}

trait S {
    type C<T>: Q;
}

fn main() {}


