tests/ui/issues/issue-8044.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-8044.rs

// pretty-expanded FIXME #23616

extern crate issue_8044 as minimal;
use minimal::{BTree, leaf};

pub fn main() {
    BTree::<isize> { node: leaf(1) };
}


