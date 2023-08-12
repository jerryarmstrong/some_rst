tests/ui/consts/const-index-feature-gate.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
const ARR: [usize; 1] = [2];
const ARR2: [i32; ARR[0]] = [5, 6];

fn main() {
}


