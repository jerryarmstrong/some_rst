tests/ui/panic_implementation-closures.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![crate_type = "rlib"]
#![no_std]

#[panic_handler]
pub fn panic_fmt(_: &::core::panic::PanicInfo) -> ! {
    |x: u8| x;
    loop {}
}


