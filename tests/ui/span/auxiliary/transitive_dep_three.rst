tests/ui/span/auxiliary/transitive_dep_three.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! define_parse_error {
    () => {
        #[macro_export]
        macro_rules! parse_error {
            () => { parse error }
        }
    }
}


