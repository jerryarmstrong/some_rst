tests/ui/panic-runtime/auxiliary/needs-abort.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=abort
// no-prefer-dynamic

#![crate_type = "rlib"]
#![no_std]


