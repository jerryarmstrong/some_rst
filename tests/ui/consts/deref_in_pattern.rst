tests/ui/consts/deref_in_pattern.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// https://github.com/rust-lang/rust/issues/25574

const A: [u8; 4] = *b"fooo";

fn main() {
    match *b"xxxx" {
        A => {},
        _ => {}
    }
}


