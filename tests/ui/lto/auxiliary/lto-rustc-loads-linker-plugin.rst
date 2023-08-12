tests/ui/lto/auxiliary/lto-rustc-loads-linker-plugin.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Clinker-plugin-lto
// no-prefer-dynamic

#![crate_type = "rlib"]

pub fn foo() {}


