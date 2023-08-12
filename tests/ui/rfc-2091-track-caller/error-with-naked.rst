tests/ui/rfc-2091-track-caller/error-with-naked.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-asm-support
#![feature(naked_functions)]

use std::arch::asm;

#[track_caller] //~ ERROR cannot use `#[track_caller]` with `#[naked]`
//~^ ERROR `#[track_caller]` requires Rust ABI
#[naked]
extern "C" fn f() {
    asm!("", options(noreturn));
}

struct S;

impl S {
    #[track_caller] //~ ERROR cannot use `#[track_caller]` with `#[naked]`
    //~^ ERROR `#[track_caller]` requires Rust ABI
    #[naked]
    extern "C" fn g() {
        asm!("", options(noreturn));
    }
}

fn main() {}


