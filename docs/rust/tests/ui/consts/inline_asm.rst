tests/ui/consts/inline_asm.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-asm-support

use std::arch::asm;

const _: () = unsafe { asm!("nop") };
//~^ ERROR inline assembly

fn main() {}


