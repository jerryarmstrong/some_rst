tests/ui/issues/issue-5521.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// aux-build:issue-5521.rs



extern crate issue_5521 as foo;

fn bar(a: foo::map) {
    if false {
        panic!();
    } else {
        let _b = &(*a)[&2];
    }
}

fn main() {}


