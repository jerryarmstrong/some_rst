tests/run-make-fulldeps/intrinsic-unreachable/exit-ret.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]
use std::arch::asm;

#[deny(unreachable_code)]
pub fn exit(n: usize) -> i32 {
    unsafe {
        // Pretend this asm is an exit() syscall.
        asm!("/*{0}*/", in(reg) n);
    }
    // This return value is just here to generate some extra code for a return
    // value, making it easier for the test script to detect whether the
    // compiler deleted it.
    42
}


