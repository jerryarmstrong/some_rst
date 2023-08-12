tests/incremental/warnings-reemitted.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: cfail1 cfail2 cfail3
// compile-flags: -Coverflow-checks=on
// build-pass

#![warn(arithmetic_overflow)]

fn main() {
    let _ = 255u8 + 1; //~ WARNING operation will overflow
}


