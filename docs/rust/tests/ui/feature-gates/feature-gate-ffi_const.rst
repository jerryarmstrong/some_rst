tests/ui/feature-gates/feature-gate-ffi_const.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

extern "C" {
    #[ffi_const] //~ ERROR the `#[ffi_const]` attribute is an experimental feature
    pub fn foo();
}


