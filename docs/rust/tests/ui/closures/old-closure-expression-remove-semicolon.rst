tests/ui/closures/old-closure-expression-remove-semicolon.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn foo() -> i32 {
    0
}

fn main() {
    let _x: i32 = {
        //~^ ERROR mismatched types
        foo(); //~ HELP remove this semicolon to return this value
    };
}


