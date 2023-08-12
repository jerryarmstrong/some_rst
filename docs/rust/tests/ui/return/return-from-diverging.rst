tests/ui/return/return-from-diverging.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that return another type in place of ! raises a type mismatch.

fn fail() -> ! {
    return "wow"; //~ ERROR mismatched types
}

fn main() {
}


