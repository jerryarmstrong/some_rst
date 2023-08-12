tests/ui/const_prop/inline_spans.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// compile-flags: -Zmir-opt-level=3
// Overflow can't be detected by const prop
// could only be detected after optimizations

#![deny(warnings)]

fn main() {
    let _ = add(u8::MAX, 1);
}

#[inline(always)]
fn add(x: u8, y: u8) -> u8 {
    x + y
}


