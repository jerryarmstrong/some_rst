tests/ui/consts/const-eval/const_fn_ptr_fail.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -Zunleash-the-miri-inside-of-you
#![allow(unused)]

fn double(x: usize) -> usize { x * 2 }
const X: fn(usize) -> usize = double;

const fn bar(x: usize) -> usize {
    X(x) // FIXME: this should error someday
}

fn main() {}


