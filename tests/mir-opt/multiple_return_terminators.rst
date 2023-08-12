tests/mir-opt/multiple_return_terminators.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z mir-opt-level=4
// EMIT_MIR multiple_return_terminators.test.MultipleReturnTerminators.diff

fn test(x: bool) {
    if x {
        // test
    } else {
        // test
    }
}

fn main() {
    test(true)
}


