tests/ui/or-patterns/mismatched-bindings-async-fn.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #71297
// edition:2018

async fn a((x | s): String) {}
//~^ ERROR variable `x` is not bound in all patterns
//~| ERROR variable `s` is not bound in all patterns

async fn b() {
    let (x | s) = String::new();
    //~^ ERROR variable `x` is not bound in all patterns
    //~| ERROR variable `s` is not bound in all patterns
}

fn main() {}


