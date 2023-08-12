tests/ui/rust-2018/auxiliary/remove-extern-crate.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! foo {
    () => ()
}

#[macro_export]
macro_rules! bar {
    () => ()
}


