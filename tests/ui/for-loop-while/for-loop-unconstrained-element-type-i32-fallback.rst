tests/ui/for-loop-while/for-loop-unconstrained-element-type-i32-fallback.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that the type of `sum` falls back to `i32` here,
// and that the for loop desugaring doesn't interfere with
// that.

fn main() {
    let mut sum = 0;
    for i in Vec::new() {
        sum += &i;
    }
}


