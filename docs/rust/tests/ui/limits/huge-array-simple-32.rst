tests/ui/limits/huge-array-simple-32.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-64bit
// build-fail

// FIXME https://github.com/rust-lang/rust/issues/59774
// normalize-stderr-test "thread.*panicked.*Metadata module not compiled.*\n" -> ""
// normalize-stderr-test "note:.*RUST_BACKTRACE=1.*\n" -> ""
#![allow(arithmetic_overflow)]

fn main() {
    let _fat: [u8; (1<<31)+(1<<15)] = //~ ERROR too big for the current architecture
        [0; (1u32<<31) as usize +(1u32<<15) as usize];
}


