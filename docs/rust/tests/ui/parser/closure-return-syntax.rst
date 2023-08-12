tests/ui/parser/closure-return-syntax.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we cannot parse a closure with an explicit return type
// unless it uses braces.

fn main() {
    let x = || -> i32 22;
    //~^ ERROR expected `{`, found `22`
}


