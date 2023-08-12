tests/run-make/wasm-symbols-not-imported/foo.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "cdylib"]
#![no_std]

use core::panic::PanicInfo;

#[no_mangle]
pub extern fn foo() {
    panic!()
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}


