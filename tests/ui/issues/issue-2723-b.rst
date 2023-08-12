tests/ui/issues/issue-2723-b.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-2723-a.rs

extern crate issue_2723_a;
use issue_2723_a::f;

pub fn main() {
    unsafe {
        f(vec![2]);
    }
}


