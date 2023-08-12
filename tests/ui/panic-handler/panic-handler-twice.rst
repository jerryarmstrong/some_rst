tests/ui/panic-handler/panic-handler-twice.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // dont-check-compiler-stderr
// aux-build:some-panic-impl.rs

#![feature(lang_items)]
#![no_std]
#![no_main]

extern crate some_panic_impl;

use core::panic::PanicInfo;

#[panic_handler]
fn panic(info: &PanicInfo) -> ! {
    //~^ ERROR found duplicate lang item `panic_impl`
    loop {}
}

#[lang = "eh_personality"]
fn eh() {}


