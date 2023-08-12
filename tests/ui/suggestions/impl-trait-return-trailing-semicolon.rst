tests/ui/suggestions/impl-trait-return-trailing-semicolon.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Bar {}

impl Bar for i32 {}

struct Qux;

impl Bar for Qux {}

fn foo() -> impl Bar {
    //~^ ERROR the trait bound `(): Bar` is not satisfied
    5;
    //~^ HELP remove this semicolon
}

fn bar() -> impl Bar {
    //~^ ERROR the trait bound `(): Bar` is not satisfied
    //~| HELP the following other types implement trait `Bar`:
    "";
}

fn main() {}


