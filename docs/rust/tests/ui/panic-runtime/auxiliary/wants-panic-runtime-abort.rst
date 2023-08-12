tests/ui/panic-runtime/auxiliary/wants-panic-runtime-abort.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=abort
// no-prefer-dynamic

#![crate_type = "rlib"]
#![no_std]

extern crate panic_runtime_abort;


