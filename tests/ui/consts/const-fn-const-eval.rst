tests/ui/consts/const-fn-const-eval.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

const fn add(x: usize, y: usize) -> usize {
    x + y
}

const ARR: [i32; add(1, 2)] = [5, 6, 7];

pub fn main() {}


