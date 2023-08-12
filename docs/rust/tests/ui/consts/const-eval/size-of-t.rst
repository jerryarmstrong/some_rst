tests/ui/consts/const-eval/size-of-t.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust/issues/69228
// Used to give bogus suggestion about T not being Sized.

use std::mem::size_of;

fn foo<T>() {
    let _arr: [u8; size_of::<T>()];
    //~^ ERROR generic parameters may not be used in const operations
    //~| NOTE cannot perform const operation
    //~| NOTE type parameters may not be used in const expressions
}

fn main() {}


