tests/ui/rust-2018/auxiliary/edition-lint-infer-outlives-macro.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn foo() {}

#[macro_export]
macro_rules! gimme_a {
    ($($mac:tt)*) => { $($mac)* { 'a } }
}


