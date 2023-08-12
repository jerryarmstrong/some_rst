tests/ui/consts/transmute-size-mismatch-before-typeck.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // normalize-stderr-64bit "64 bits" -> "word size"
// normalize-stderr-32bit "32 bits" -> "word size"
// normalize-stderr-64bit "128 bits" -> "2 * word size"
// normalize-stderr-32bit "64 bits" -> "2 * word size"

fn main() {
    match &b""[..] {
        ZST => {}
    }
}

const ZST: &[u8] = unsafe { std::mem::transmute(1usize) };
//~^ ERROR cannot transmute between types of different sizes


