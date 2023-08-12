tests/ui/coercion/coerce-reborrow-imm-vec-arg.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

fn sum(x: &[isize]) -> isize {
    let mut sum = 0;
    for y in x { sum += *y; }
    return sum;
}

fn sum_mut(y: &mut [isize]) -> isize {
    sum(y)
}

fn sum_imm(y: &[isize]) -> isize {
    sum(y)
}

pub fn main() {}


