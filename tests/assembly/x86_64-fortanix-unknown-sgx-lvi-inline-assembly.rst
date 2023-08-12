tests/assembly/x86_64-fortanix-unknown-sgx-lvi-inline-assembly.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test LVI load hardening on SGX inline assembly code

// assembly-output: emit-asm
// compile-flags: --crate-type staticlib
// only-x86_64-fortanix-unknown-sgx

use std::arch::asm;

#[no_mangle]
pub extern "C" fn get(ptr: *const u64) -> u64 {
    let value: u64;
    unsafe {
        asm!(".start_inline_asm:",
            "mov {}, [{}]",
            ".end_inline_asm:",
            out(reg) value,
            in(reg) ptr);
    }
    value
}

// CHECK: get
// CHECK: .start_inline_asm
// CHECK-NEXT: movq
// CHECK-NEXT: lfence
// CHECK-NEXT: .end_inline_asm

#[no_mangle]
pub extern "C" fn myret() {
    unsafe {
        asm!(
            ".start_myret_inline_asm:",
            "ret",
            ".end_myret_inline_asm:",
        );
    }
}

// CHECK: myret
// CHECK: .start_myret_inline_asm
// CHECK-NEXT: shlq $0, (%rsp)
// CHECK-NEXT: lfence
// CHECK-NEXT: retq


