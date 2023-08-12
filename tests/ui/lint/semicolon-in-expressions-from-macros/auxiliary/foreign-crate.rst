tests/ui/lint/semicolon-in-expressions-from-macros/auxiliary/foreign-crate.rs
=============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! my_macro {
    () => { true; }
}


