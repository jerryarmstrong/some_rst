src/tools/clippy/tests/ui/zero_div_zero.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(unused_variables, clippy::eq_op)]
#[warn(clippy::zero_divided_by_zero)]
fn main() {
    let nan = 0.0 / 0.0;
    let f64_nan = 0.0 / 0.0f64;
    let other_f64_nan = 0.0f64 / 0.0;
    let one_more_f64_nan = 0.0f64 / 0.0f64;
    let zero = 0.0;
    let other_zero = 0.0;
    let other_nan = zero / other_zero; // fine - this lint doesn't propagate constants.
    let not_nan = 2.0 / 0.0; // not an error: 2/0 = inf
    let also_not_nan = 0.0 / 2.0; // not an error: 0/2 = 0
}


