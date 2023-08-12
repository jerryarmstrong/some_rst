tests/ui/consts/refs_check_const_value_eq-issue-88876.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![allow(incomplete_features)]
#![feature(adt_const_params)]

struct FooConst<const ARRAY: &'static [&'static str]> {}

const FOO_ARR: &[&'static str; 2] = &["Hello", "Friend"];

fn main() {
    let _ = FooConst::<FOO_ARR> {};
}


