tests/ui/suggestions/dont-suggest-try_into-in-macros.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    assert_eq!(10u64, 10usize); //~ ERROR mismatched types
}


