tests/ui/closures/2229_closure_analysis/run_pass/capture-disjoint-field-tuple.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// run-pass

// Test that we can immutably borrow an element of a tuple from within a closure,
// while having a mutable borrow to another element of the same tuple outside the closure.

#![feature(rustc_attrs)]

fn main() {
    let mut t = (10, 10);

    let c = || {
        println!("{}", t.0);
    };

    // `c` only captures t.0, therefore mutating t.1 is allowed.
    let t1 = &mut t.1;

    c();
    *t1 = 20;
}


