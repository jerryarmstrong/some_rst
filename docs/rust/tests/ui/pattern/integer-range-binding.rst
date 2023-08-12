tests/ui/pattern/integer-range-binding.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn main() {
    let -2147483648..=2147483647 = 1;
    let 0..=255 = 0u8;
    let -128..=127 = 0i8;
    let '\u{0000}'..='\u{10FFFF}' = 'v';
}


