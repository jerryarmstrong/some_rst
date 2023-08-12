tests/ui/issues/issue-66667-function-cmp-cycle.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn first() {
    second == 1 //~ ERROR binary operation
    //~^ ERROR mismatched types
}

fn second() {
    first == 1 //~ ERROR binary operation
    //~^ ERROR mismatched types
}

fn bar() {
    bar == 1 //~ ERROR binary operation
    //~^ ERROR mismatched types
}

fn main() {}


