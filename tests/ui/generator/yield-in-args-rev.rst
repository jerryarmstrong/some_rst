tests/ui/generator/yield-in-args-rev.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

// Test that a borrow that occurs after a yield in the same
// argument list is not treated as live across the yield by
// type-checking.

#![feature(generators)]

fn foo(_a: (), _b: &bool) {}

fn bar() {
    || { //~ WARN unused generator that must be used
        let b = true;
        foo(yield, &b);
    };
}

fn main() { }


