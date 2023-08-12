tests/ui/unique/unique-decl.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]


pub fn main() {
    let _: Box<isize>;
}

fn f(_i: Box<isize>) -> Box<isize> {
    panic!();
}


