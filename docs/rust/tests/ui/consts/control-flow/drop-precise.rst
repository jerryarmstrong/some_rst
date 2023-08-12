tests/ui/consts/control-flow/drop-precise.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// gate-test-const_precise_live_drops

#![feature(const_precise_live_drops)]

const _: Vec<i32> = {
    let vec_tuple = (Vec::new(),);
    vec_tuple.0
};

const _: Vec<i32> = {
    let x: Result<_, Vec<i32>> = Ok(Vec::new());
    match x {
        Ok(x) | Err(x) => x,
    }
};

fn main() {}


