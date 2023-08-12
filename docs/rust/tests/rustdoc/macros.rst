tests/rustdoc/macros.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has macros/macro.my_macro.html //pre 'macro_rules! my_macro {'
// @has - //pre '() => { ... };'
// @has - //pre '($a:tt) => { ... };'
// @has - //pre '($e:expr) => { ... };'
#[macro_export]
macro_rules! my_macro {
    () => [];
    ($a:tt) => ();
    ($e:expr) => {};
}

// Check that exported macro defined in a module are shown at crate root.
// @has macros/macro.my_sub_macro.html //pre 'macro_rules! my_sub_macro {'
// @has - //pre '() => { ... };'
// @has - //pre '($a:tt) => { ... };'
// @has - //pre '($e:expr) => { ... };'
mod sub {
    #[macro_export]
    macro_rules! my_sub_macro {
        () => {};
        ($a:tt) => {};
        ($e:expr) => {};
    }
}


