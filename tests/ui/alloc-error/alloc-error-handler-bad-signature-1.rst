tests/ui/alloc-error/alloc-error-handler-bad-signature-1.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=abort

#![feature(alloc_error_handler)]
#![no_std]
#![no_main]

use core::alloc::Layout;

#[alloc_error_handler]
fn oom(
    info: &Layout, //~^ ERROR mismatched types
) -> () //~^^ ERROR mismatched types
{
    loop {}
}

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! { loop {} }


