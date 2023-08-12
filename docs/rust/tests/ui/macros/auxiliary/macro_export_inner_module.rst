tests/ui/macros/auxiliary/macro_export_inner_module.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod inner {
    #[macro_export]
    macro_rules! foo {
        () => (1)
    }
}


