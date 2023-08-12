tests/ui/unsafe/inline_asm.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck
// needs-asm-support

use std::arch::asm;

fn main() {
    asm!("nop"); //~ ERROR use of inline assembly is unsafe and requires unsafe function or block
}


