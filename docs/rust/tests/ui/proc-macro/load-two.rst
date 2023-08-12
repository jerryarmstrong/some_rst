tests/ui/proc-macro/load-two.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(path_statements)]
#![allow(dead_code)]
// aux-build:derive-atob.rs
// aux-build:derive-ctod.rs

#[macro_use]
extern crate derive_atob;
#[macro_use]
extern crate derive_ctod;

#[derive(Copy, Clone)]
#[derive(AToB)]
struct A;

#[derive(CToD)]
struct C;

fn main() {
    B;
    D;
}


