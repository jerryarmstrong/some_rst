tests/ui/issues/issue-5844.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //aux-build:issue-5844-aux.rs
// revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

extern crate issue_5844_aux;

fn main () {
    issue_5844_aux::rand(); //~ ERROR: requires unsafe
}


