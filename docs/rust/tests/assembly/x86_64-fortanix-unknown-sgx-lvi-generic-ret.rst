tests/assembly/x86_64-fortanix-unknown-sgx-lvi-generic-ret.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test LVI ret hardening on generic rust code

// assembly-output: emit-asm
// compile-flags: --crate-type staticlib
// only-x86_64-fortanix-unknown-sgx

#[no_mangle]
pub extern fn myret() {}
// CHECK: myret:
// CHECK: popq [[REGISTER:%[a-z]+]]
// CHECK-NEXT: lfence
// CHECK-NEXT: jmpq *[[REGISTER]]


