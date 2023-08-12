tests/assembly/aarch64-pointer-auth.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that PAC instructions are emitted when branch-protection is specified.

// assembly-output: emit-asm
// compile-flags: --target aarch64-unknown-linux-gnu
// compile-flags: -Z branch-protection=pac-ret,leaf
// needs-llvm-components: aarch64

#![feature(no_core, lang_items)]
#![no_std]
#![no_core]
#![crate_type = "lib"]

#[lang = "sized"]
trait Sized {}

// CHECK: hint #25
// CHECK: hint #29
#[no_mangle]
pub fn test() -> u8 {
    42
}


