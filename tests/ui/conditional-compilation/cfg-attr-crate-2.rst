tests/ui/conditional-compilation/cfg-attr-crate-2.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust/issues/21833#issuecomment-72353044

// compile-flags: --cfg broken

#![crate_type = "lib"]
#![cfg_attr(broken, no_core)] //~ ERROR the `#[no_core]` attribute is an experimental feature

pub struct S {}


