tests/ui/proc-macro/bang-macro.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:bang-macro.rs

extern crate bang_macro;
use bang_macro::rewrite;

fn main() {
    assert_eq!(rewrite!("Hello, world!"), "NOT Hello, world!");
}


