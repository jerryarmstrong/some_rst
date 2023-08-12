tests/mir-opt/tls_access.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // EMIT_MIR tls_access.main.PreCodegen.after.mir
// compile-flags: -Zmir-opt-level=0

#![feature(thread_local)]

#[thread_local]
static mut FOO: u8 = 3;

fn main() {
    unsafe {
        let a = &FOO;
        FOO = 42;
    }
}


