tests/ui/panic-handler/panic-handler-bad-signature-2.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C panic=abort

#![no_std]
#![no_main]

use core::panic::PanicInfo;

#[panic_handler]
fn panic(
    info: &'static PanicInfo, //~ ERROR argument should be `&PanicInfo`
) -> !
{
    loop {}
}


