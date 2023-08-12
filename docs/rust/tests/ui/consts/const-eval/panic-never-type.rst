tests/ui/consts/const-eval/panic-never-type.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #66975
#![feature(never_type)]

const VOID: ! = panic!();
//~^ ERROR evaluation of constant value failed

fn main() {
    let _ = VOID;
}


