tests/mir-opt/inline/asm_unwind.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests inlining of `may_unwind` inline assembly.
//
// ignore-wasm32-bare compiled with panic=abort by default
// needs-asm-support
#![feature(asm_unwind)]

struct D;

impl Drop for D {
    fn drop(&mut self) {}
}

#[inline(always)]
fn foo() {
    let _d = D;
    unsafe { std::arch::asm!("", options(may_unwind)) };
}

// EMIT_MIR asm_unwind.main.Inline.diff
pub fn main() {
    foo();
}


