tests/ui/parser/macro/trait-object-macro-matcher.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // A single lifetime is not parsed as a type.
// `ty` matcher in particular doesn't accept a single lifetime

macro_rules! m {
    ($t: ty) => {
        let _: $t;
    };
}

fn main() {
    m!('static);
    //~^ ERROR lifetime in trait object type must be followed by `+`
    //~| ERROR at least one trait is required for an object type
}


