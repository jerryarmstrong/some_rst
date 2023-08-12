tests/ui/mismatched_types/float-literal-inference-restrictions.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: f32 = 1; //~ ERROR mismatched types
    let y: f32 = 1f64; //~ ERROR mismatched types
}


