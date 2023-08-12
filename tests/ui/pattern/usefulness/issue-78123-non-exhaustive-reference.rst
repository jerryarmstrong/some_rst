tests/ui/pattern/usefulness/issue-78123-non-exhaustive-reference.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum A {}
    //~^ NOTE `A` defined here
    //~| NOTE

fn f(a: &A) {
    match a {}
    //~^ ERROR non-exhaustive patterns: type `&A` is non-empty
    //~| NOTE the matched value is of type `&A`
    //~| NOTE references are always considered inhabited
}

fn main() {}


