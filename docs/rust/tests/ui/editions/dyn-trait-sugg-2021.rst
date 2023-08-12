tests/ui/editions/dyn-trait-sugg-2021.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

trait Foo<T> {}

impl<T> dyn Foo<T> {
    fn hi(_x: T) {}
}

fn main() {
    Foo::hi(123);
    //~^ ERROR trait objects must include the `dyn` keyword
}


