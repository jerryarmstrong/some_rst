tests/ui/asm/noreturn.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-asm-support
// check-pass

#![feature(never_type)]
#![crate_type = "rlib"]

use std::arch::asm;

pub unsafe fn asm1() {
    let _: () = asm!("");
}

pub unsafe fn asm2() {
    let _: ! = asm!("", options(noreturn));
}

pub unsafe fn asm3() -> ! {
    asm!("", options(noreturn));
}


