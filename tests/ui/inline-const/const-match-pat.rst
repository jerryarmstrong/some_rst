tests/ui/inline-const/const-match-pat.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(incomplete_features)]
#![feature(inline_const_pat)]
const MMIO_BIT1: u8 = 4;
const MMIO_BIT2: u8 = 5;

fn main() {
    let s = match read_mmio() {
        0 => "FOO",
        const { 1 << MMIO_BIT1 } => "BAR",
        const { 1 << MMIO_BIT2 } => "BAZ",
        _ => unreachable!(),
    };

    assert_eq!("BAZ", s);
}

fn read_mmio() -> i32 {
    1 << 5
}


