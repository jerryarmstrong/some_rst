tests/ui/lto/lto-opt-level-s.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Clinker-plugin-lto -Copt-level=s
// build-pass
// no-prefer-dynamic

#![crate_type = "rlib"]

pub fn foo() {}


