tests/ui/feature-gates/feature-gate-collapse_debuginfo.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[collapse_debuginfo]
//~^ ERROR the `#[collapse_debuginfo]` attribute is an experimental feature
macro_rules! foo {
    ($e:expr) => { $e }
}

fn main() {}


