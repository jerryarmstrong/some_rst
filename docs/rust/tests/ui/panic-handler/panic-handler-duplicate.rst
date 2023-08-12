tests/ui/panic-handler/panic-handler-duplicate.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=abort

#![feature(lang_items)]
#![no_std]
#![no_main]

use core::panic::PanicInfo;

#[panic_handler]
fn panic(info: &PanicInfo) -> ! {
    loop {}
}

#[lang = "panic_impl"]
fn panic2(info: &PanicInfo) -> ! { //~ ERROR found duplicate lang item `panic_impl`
    loop {}
}


