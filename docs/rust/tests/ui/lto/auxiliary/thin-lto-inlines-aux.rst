tests/ui/lto/auxiliary/thin-lto-inlines-aux.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

#![crate_type = "rlib"]

pub fn bar() -> u32 {
    3
}


