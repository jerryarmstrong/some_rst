tests/mir-opt/equal_true.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test InstCombine

// EMIT_MIR equal_true.opt.InstCombine.diff

fn opt(x: bool) -> i32 {
    if x == true { 0 } else { 1 }
}

fn main() {
    opt(true);
}


