tests/ui/issues/issue-6919.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_attributes)]
// aux-build:iss.rs

// pretty-expanded FIXME #23616

extern crate issue6919_3;

pub fn main() {
    let _ = issue6919_3::D.k;
}


