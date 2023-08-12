tests/ui/macros/auxiliary/define-macro.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! define_macro {
    ($i:ident) => {
        macro_rules! $i { () => {} }
    }
}


