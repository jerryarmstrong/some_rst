tests/ui/feature-gates/feature-gate-ffi_returns_twice.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

extern "C" {
    #[ffi_returns_twice] //~ ERROR the `#[ffi_returns_twice]` attribute is an experimental feature
    pub fn foo();
}


