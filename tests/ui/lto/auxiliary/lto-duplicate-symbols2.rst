tests/ui/lto/auxiliary/lto-duplicate-symbols2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic

#![crate_type = "rlib"]

#[no_mangle]
pub extern "C" fn foo() {}


