tests/ui/proc-macro/expand-with-a-macro.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// needs-unwind
// aux-build:expand-with-a-macro.rs


#![deny(warnings)]

#[macro_use]
extern crate expand_with_a_macro;

use std::panic;

#[derive(A)]
struct A;

fn main() {
    assert!(panic::catch_unwind(|| {
        A.a();
    }).is_err());
}


