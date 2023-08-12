tests/ui/consts/miri_unleashed/inline_asm.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunleash-the-miri-inside-of-you
// only-x86_64

use std::arch::asm;

fn main() {}

// Make sure we catch executing inline assembly.
static TEST_BAD: () = {
    unsafe { asm!("nop"); }
    //~^ ERROR could not evaluate static initializer
    //~| NOTE inline assembly is not supported
};


