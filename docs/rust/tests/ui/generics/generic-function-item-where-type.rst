tests/ui/generics/generic-function-item-where-type.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<U>() {}

fn main() {
    foo::<main>()
    //~^ ERROR constant provided when a type was expected
}


