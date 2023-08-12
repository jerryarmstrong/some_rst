tests/ui/suggestions/return-closures.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    //~^ HELP try adding a return type
    |x: &i32| 1i32
    //~^ ERROR mismatched types
}

fn bar(i: impl Sized) {
    //~^ HELP a return type might be missing here
    || i
    //~^ ERROR mismatched types
}

fn main() {}


