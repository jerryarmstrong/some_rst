tests/ui/empty_global_asm.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-asm-support
// run-pass

use std::arch::global_asm;

global_asm!("");

fn main() {}


