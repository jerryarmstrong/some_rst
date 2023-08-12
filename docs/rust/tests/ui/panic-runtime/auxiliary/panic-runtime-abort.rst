tests/ui/panic-runtime/auxiliary/panic-runtime-abort.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=abort
// no-prefer-dynamic

#![feature(panic_runtime)]
#![crate_type = "rlib"]

#![no_std]
#![panic_runtime]

#[no_mangle]
pub extern "C" fn __rust_maybe_catch_panic() {}

#[no_mangle]
pub extern "C" fn __rust_start_panic() {}

#[no_mangle]
pub extern "C" fn rust_eh_personality() {}


