src/tools/clippy/clippy_utils/src/sym_helper.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
/// Convenience wrapper around rustc's `Symbol::intern`
macro_rules! sym {
    ($tt:tt) => {
        rustc_span::symbol::Symbol::intern(stringify!($tt))
    };
}


