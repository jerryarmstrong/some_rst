tests/rustdoc-ui/auxiliary/panic-item.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
#![crate_type = "lib"]
#![no_std]
#![feature(lang_items)]

use core::panic::PanicInfo;
use core::sync::atomic::{self, Ordering};

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {
        atomic::compiler_fence(Ordering::SeqCst);
    }
}

#[lang = "eh_personality"]
fn foo() {}


