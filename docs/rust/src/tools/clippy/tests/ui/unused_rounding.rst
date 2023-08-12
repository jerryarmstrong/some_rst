src/tools/clippy/tests/ui/unused_rounding.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![warn(clippy::unused_rounding)]

fn main() {
    let _ = 1f32.ceil();
    let _ = 1.0f64.floor();
    let _ = 1.00f32.round();
    let _ = 2e-54f64.floor();

    // issue9866
    let _ = 3.3_f32.round();
    let _ = 3.3_f64.round();
    let _ = 3.0_f32.round();

    let _ = 3_3.0_0_f32.round();
    let _ = 3_3.0_1_f64.round();
}


