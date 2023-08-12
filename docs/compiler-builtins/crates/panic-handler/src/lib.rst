crates/panic-handler/src/lib.rs
===============================

Last edited: 2023-03-09 18:36:25

Contents:

.. code-block:: rs

    //! This is needed for tests on targets that require a `#[panic_handler]` function

#![feature(no_core)]
#![no_core]

extern crate core;

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! {
    loop {}
}


