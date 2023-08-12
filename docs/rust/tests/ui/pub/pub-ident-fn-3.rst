tests/ui/pub/pub-ident-fn-3.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // #60115

mod foo {
    pub bar();
    //~^ ERROR missing `fn` or `struct` for function or struct definition
}

fn main() {}


