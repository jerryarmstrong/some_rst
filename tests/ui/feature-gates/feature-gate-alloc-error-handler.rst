tests/ui/feature-gates/feature-gate-alloc-error-handler.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=abort

#![no_std]
#![no_main]

use core::alloc::Layout;

#[alloc_error_handler] //~ ERROR use of unstable library feature 'alloc_error_handler'
fn oom(info: Layout) -> ! {
    loop {}
}

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! {
    loop {}
}


