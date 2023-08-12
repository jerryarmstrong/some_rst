tests/ui/proc-macro/derive-same-struct.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(path_statements)]
#![allow(dead_code)]
// aux-build:derive-same-struct.rs

#[macro_use]
extern crate derive_same_struct;

#[derive(AToB)]
struct A;

fn main() {
    C;
}


