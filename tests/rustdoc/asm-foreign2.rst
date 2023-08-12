tests/rustdoc/asm-foreign2.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-aarch64
// Make sure rustdoc accepts options(att_syntax) asm! on non-x86 targets.

use std::arch::asm;

// @has asm_foreign2/fn.x86.html
pub unsafe fn x86(x: i64) -> i64 {
    let y;
    asm!("movq {}, {}", in(reg) x, out(reg) y, options(att_syntax));
    y
}


