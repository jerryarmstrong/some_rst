src/tools/clippy/tests/ui/as_underscore.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::as_underscore)]

fn foo(_n: usize) {}

fn main() {
    let n: u16 = 256;
    foo(n as _);

    let n = 0_u128;
    let _n: u8 = n as _;
}


