tests/ui/closures/semistatement-in-lambda.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_must_use)]

pub fn main() {
    // Test that lambdas behave as unary expressions with block-like expressions
    -if true { 1 } else { 2 } * 3;
    || if true { 1 } else { 2 } * 3;

    // The following is invalid and parses as `if true { 1 } else { 2 }; *3`
    // if true { 1 } else { 2 } * 3
}


