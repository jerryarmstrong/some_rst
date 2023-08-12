tests/ui/mismatched_types/for-loop-has-unit-body.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    for x in 0..3 {
        x //~ ERROR mismatched types
    }
}


