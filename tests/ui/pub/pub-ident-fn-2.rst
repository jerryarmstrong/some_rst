tests/ui/pub/pub-ident-fn-2.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

pub foo(_s: usize) { bar() }
//~^ ERROR missing `fn` for function definition

fn bar() {}

fn main() {
    foo(2);
}


