tests/ui/consts/const-eval/panic-assoc-never-type.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

// Regression test for #66975
#![feature(never_type)]

struct PrintName;

impl PrintName {
    const VOID: ! = panic!();
    //~^ ERROR evaluation of constant value failed
}

fn main() {
    let _ = PrintName::VOID; //~ constant
}


