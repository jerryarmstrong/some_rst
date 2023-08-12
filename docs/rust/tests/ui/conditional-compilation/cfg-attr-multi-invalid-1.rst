tests/ui/conditional-compilation/cfg-attr-multi-invalid-1.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --cfg broken

#![crate_type = "lib"]
#![cfg_attr(broken, no_core, no_std)]
//~^ ERROR the `#[no_core]` attribute is an experimental feature

pub struct S {}


