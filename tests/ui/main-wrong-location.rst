tests/ui/main-wrong-location.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod m {
    // An inferred main entry point
    // must appear at the top of the crate
    fn main() { }
} //~ ERROR `main` function not found


