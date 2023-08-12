tests/ui/suggestions/unnecessary_dot_for_floating_point_literal.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _: f64 = 0..10; //~ ERROR mismatched types
    let _: f64 = 1..; //~ ERROR mismatched types
    let _: f64 = ..10; //~ ERROR mismatched types
    let _: f64 = std::ops::Range { start: 0, end: 1 }; //~ ERROR mismatched types
}


