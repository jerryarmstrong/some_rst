tests/mir-opt/not_equal_false.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: InstCombine
// EMIT_MIR not_equal_false.opt.InstCombine.diff

fn opt(x: bool) -> u32 {
    if x != false { 0 } else { 1 }
}

fn main() {
    opt(false);
}


