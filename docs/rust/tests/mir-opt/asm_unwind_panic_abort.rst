tests/mir-opt/asm_unwind_panic_abort.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Tests that unwinding from an asm block is caught and forced to abort
//! when `-C panic=abort`.

// only-x86_64
// compile-flags: -C panic=abort
// no-prefer-dynamic

#![feature(asm_unwind)]

// EMIT_MIR asm_unwind_panic_abort.main.AbortUnwindingCalls.after.mir
fn main() {
    unsafe {
        std::arch::asm!("", options(may_unwind));
    }
}


