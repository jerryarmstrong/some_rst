tests/ui/mismatched_types/closure-mismatch.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {}

impl<T: Fn(&())> Foo for T {}

fn baz<T: Foo>(_: T) {}

fn main() {
    baz(|_| ());
    //~^ ERROR implementation of `FnOnce` is not general enough
    //~| ERROR mismatched types
}


