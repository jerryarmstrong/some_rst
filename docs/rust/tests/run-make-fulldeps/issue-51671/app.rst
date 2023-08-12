tests/run-make-fulldeps/issue-51671/app.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "bin"]
#![feature(lang_items, alloc_error_handler)]
#![no_main]
#![no_std]

use core::alloc::Layout;
use core::panic::PanicInfo;

#[panic_handler]
fn panic(_: &PanicInfo) -> ! {
    loop {}
}

#[lang = "eh_personality"]
fn eh() {}

#[alloc_error_handler]
fn oom(_: Layout) -> ! {
    loop {}
}


