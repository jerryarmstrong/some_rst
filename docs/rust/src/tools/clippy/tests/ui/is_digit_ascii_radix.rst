src/tools/clippy/tests/ui/is_digit_ascii_radix.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::is_digit_ascii_radix)]

const TEN: u32 = 10;

fn main() {
    let c: char = '6';

    // Should trigger the lint.
    let _ = c.is_digit(10);
    let _ = c.is_digit(16);
    let _ = c.is_digit(0x10);

    // Should not trigger the lint.
    let _ = c.is_digit(11);
    let _ = c.is_digit(TEN);
}


