tests/ui/proc-macro/smoke.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_must_use)]
#![allow(path_statements)]
// aux-build:derive-a.rs

#[macro_use]
extern crate derive_a;

#[derive(Debug, PartialEq, A, Eq, Copy, Clone)]
struct A;

fn main() {
    A;
    assert_eq!(A, A);
    A.clone();
    let a = A;
    let _c = a;
    let _d = a;
}


