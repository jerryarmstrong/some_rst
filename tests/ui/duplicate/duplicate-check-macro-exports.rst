tests/ui/duplicate/duplicate-check-macro-exports.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub use std::panic;

#[macro_export]
macro_rules! panic { () => {} } //~ ERROR the name `panic` is defined multiple times

fn main() {}


