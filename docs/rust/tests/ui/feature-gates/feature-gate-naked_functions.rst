tests/ui/feature-gates/feature-gate-naked_functions.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-asm-support

use std::arch::asm;

#[naked]
//~^ the `#[naked]` attribute is an experimental feature
extern "C" fn naked() {
    asm!("", options(noreturn))
}

#[naked]
//~^ the `#[naked]` attribute is an experimental feature
extern "C" fn naked_2() -> isize {
    asm!("", options(noreturn))
}

fn main() {}


