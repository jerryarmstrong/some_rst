src/lib.rs
==========

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: rs

    #![no_std]

use core::panic::PanicInfo;

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}



