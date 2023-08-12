tests/ui/issues/issue-7899.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
// aux-build:issue-7899.rs

// pretty-expanded FIXME #23616

extern crate issue_7899 as testcrate;

fn main() {
    let f = testcrate::V2(1.0f32, 2.0f32);
}


