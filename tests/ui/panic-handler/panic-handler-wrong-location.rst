tests/ui/panic-handler/panic-handler-wrong-location.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=abort

#![no_std]
#![no_main]

#[panic_handler] //~ ERROR `panic_impl` language item must be applied to a function
#[no_mangle]
static X: u32 = 42;


