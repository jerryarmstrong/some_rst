tests/ui/issues/issue-2526-a.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-2526.rs

// pretty-expanded FIXME #23616

#![allow(unused_imports)]

extern crate issue_2526;
use issue_2526::*;

pub fn main() {}


