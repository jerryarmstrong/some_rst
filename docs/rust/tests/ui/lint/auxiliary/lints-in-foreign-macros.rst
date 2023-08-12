tests/ui/lint/auxiliary/lints-in-foreign-macros.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! bar {
    () => {use std::string::ToString;}
}

#[macro_export]
macro_rules! baz {
    ($i:item) => ($i)
}

#[macro_export]
macro_rules! baz2 {
    ($($i:tt)*) => ($($i)*)
}


