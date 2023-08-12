tests/ui/numbers-arithmetic/u32-decr.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass




pub fn main() {
    let mut word: u32 = 200000;
    word = word - 1;
    assert_eq!(word, 199999);
}


