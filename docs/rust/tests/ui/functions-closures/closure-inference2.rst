tests/ui/functions-closures/closure-inference2.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test a rather underspecified example:
#![allow(unused_braces)]

pub fn main() {
    let f = {|i| i};
    assert_eq!(f(2), 2);
    assert_eq!(f(5), 5);
}


