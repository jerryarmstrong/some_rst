tests/ui/suggestions/call-on-unimplemented-with-autoderef.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {}

impl Foo for i32 {}

fn needs_foo(_: impl Foo) {}

fn test(x: &Box<dyn Fn() -> i32>) {
    needs_foo(x);
    //~^ ERROR the trait bound
    //~| HELP use parentheses to call this trait object
}

fn main() {}


