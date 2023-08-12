tests/ui/array-slice-vec/array_const_index-2.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(stable_features)]

#![feature(const_indexing)]

fn main() {
    const ARR: [i32; 6] = [42, 43, 44, 45, 46, 47];
    const IDX: usize = 3;
    const VAL: i32 = ARR[IDX];
    const BLUB: [i32; (ARR[0] - 41) as usize] = [5];
}


