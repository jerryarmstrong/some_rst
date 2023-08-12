src/tools/clippy/tests/ui/char_lit_as_u8_suggestions.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::char_lit_as_u8)]

fn main() {
    let _ = 'a' as u8;
    let _ = '\n' as u8;
    let _ = '\0' as u8;
    let _ = '\x01' as u8;
}


