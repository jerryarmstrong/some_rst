tests/ui/path-lookahead.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// run-rustfix

#![allow(dead_code)]
#![warn(unused_parens)]

// Parser test for #37765

fn with_parens<T: ToString>(arg: T) -> String {
    return (<T as ToString>::to_string(&arg)); //~WARN unnecessary parentheses around `return` value
}

fn no_parens<T: ToString>(arg: T) -> String {
    return <T as ToString>::to_string(&arg);
}

fn main() {}


