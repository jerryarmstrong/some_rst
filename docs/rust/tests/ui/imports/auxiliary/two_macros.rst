tests/ui/imports/auxiliary/two_macros.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! m { ($($t:tt)*) => { $($t)* } }

#[macro_export]
macro_rules! n { ($($t:tt)*) => { $($t)* } }


