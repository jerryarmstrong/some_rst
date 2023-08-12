src/tools/clippy/tests/ui/char_lit_as_u8.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::char_lit_as_u8)]

fn main() {
    let _ = '❤' as u8; // no suggestion, since a byte literal won't work.
}


