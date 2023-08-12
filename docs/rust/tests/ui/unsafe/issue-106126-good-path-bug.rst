tests/ui/unsafe/issue-106126-good-path-bug.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #106126.
// check-pass
// aux-build:issue-106126.rs

#![deny(unsafe_op_in_unsafe_fn)]

#[macro_use]
extern crate issue_106126;

foo!();

fn main() {}


