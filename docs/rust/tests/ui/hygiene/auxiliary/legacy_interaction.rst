tests/ui/hygiene/auxiliary/legacy_interaction.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-pretty pretty-printing is unhygienic

#[macro_export]
macro_rules! m {
    () => {
        fn f() {} // (2)
        g(); // (1)
    }
}


