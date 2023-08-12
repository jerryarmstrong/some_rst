src/tools/clippy/tests/ui-toml/disallowed_macros/auxiliary/macros.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! expr {
    () => {
        1
    };
}

#[macro_export]
macro_rules! stmt {
    () => {
        let _x = ();
    };
}

#[macro_export]
macro_rules! ty {
    () => { &'static str };
}

#[macro_export]
macro_rules! pat {
    () => {
        _
    };
}

#[macro_export]
macro_rules! item {
    () => {
        const ITEM: usize = 1;
    };
}


