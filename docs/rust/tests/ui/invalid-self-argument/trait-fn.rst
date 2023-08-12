tests/ui/invalid-self-argument/trait-fn.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {}

impl Foo {
    fn c(foo: u32, self) {}
    //~^ ERROR unexpected `self` parameter in function
    //~| NOTE must be the first parameter of an associated function

    fn good(&mut self, foo: u32) {}
}

fn main() { }


