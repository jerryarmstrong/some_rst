tests/ui/consts/const-unwrap.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

#![feature(const_option)]

const FOO: i32 = Some(42i32).unwrap();

const BAR: i32 = Option::<i32>::None.unwrap();
//~^ERROR: evaluation of constant value failed

fn main() {
    println!("{}", FOO);
    println!("{}", BAR);
}


