tests/ui/macros/auxiliary/macro-in-other-crate.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! mac {
    ($ident:ident) => { let $ident = 42; }
}

#[macro_export]
macro_rules! inline {
    () => ()
}

#[macro_export]
macro_rules! from_prelude {
    () => ()
}


