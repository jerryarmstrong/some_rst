tests/ui/asm/x86_64/multiple-clobber-abi.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// needs-asm-support
// only-x86_64

// Checks that multiple clobber_abi options can be used

use std::arch::asm;

extern "sysv64" fn foo(x: i32) -> i32 {
    x + 16
}

extern "win64" fn bar(x: i32) -> i32 {
    x / 2
}

fn main() {
    let x = 8;
    let y: i32;
    // call `foo` with `x` as the input, and then `bar` with the output of `foo`
    // and output that to `y`
    unsafe {
        asm!(
            "call {}; mov rcx, rax; call {}",
            sym foo,
            sym bar,
            in("rdi") x,
            out("rax") y,
            clobber_abi("sysv64", "win64"),
        );
    }
    assert_eq!((x, y), (8, 12));
}


