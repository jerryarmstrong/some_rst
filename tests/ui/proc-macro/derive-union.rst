tests/ui/proc-macro/derive-union.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_variables)]
// aux-build:derive-union.rs

#[macro_use]
extern crate derive_union;

#[repr(C)]
#[derive(UnionTest)]
union Test {
    a: u8,
}

fn main() {
    let t = Test { a: 0 };
}


