tests/ui/imports/extern-crate-self/extern-crate-self-macro-self.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// Test that a macro can correctly expand `self` in
// an `extern crate self as ALIAS` item.

fn the_answer() -> usize { 42 }

macro_rules! extern_something {
    ($alias:ident) => { extern crate $alias as the_alias; }
}

extern_something!(self);

fn main() {
    assert_eq!(the_alias::the_answer(), 42);
}


