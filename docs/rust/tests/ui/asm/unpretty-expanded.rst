tests/ui/asm/unpretty-expanded.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // needs-asm-support
// check-pass
// compile-flags: -Zunpretty=expanded
core::arch::global_asm!("x: .byte 42");


