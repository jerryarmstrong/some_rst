tests/ui/macros/auxiliary/use-macro-self.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod foobarius {}

#[macro_export]
macro_rules! foobarius {
    () => { () }
}


