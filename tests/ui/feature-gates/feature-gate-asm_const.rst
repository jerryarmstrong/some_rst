tests/ui/feature-gates/feature-gate-asm_const.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // only-x86_64

use std::arch::asm;

unsafe fn foo<const N: usize>() {
    asm!("mov eax, {}", const N + 1);
    //~^ ERROR const operands for inline assembly are unstable
}

fn main() {
    unsafe {
        foo::<0>();
        asm!("mov eax, {}", const 123);
        //~^ ERROR const operands for inline assembly are unstable
    }
}


