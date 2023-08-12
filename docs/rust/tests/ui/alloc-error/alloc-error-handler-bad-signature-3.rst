tests/ui/alloc-error/alloc-error-handler-bad-signature-3.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=abort

#![feature(alloc_error_handler)]
#![no_std]
#![no_main]

struct Layout;

#[alloc_error_handler]
fn oom() -> ! { //~ ERROR function takes 0 arguments but 1 argument was supplied
    loop {}
}

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! { loop {} }


