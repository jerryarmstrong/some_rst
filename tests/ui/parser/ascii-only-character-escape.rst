tests/ui/parser/ascii-only-character-escape.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = "\x80"; //~ ERROR out of range hex escape
    let y = "\xff"; //~ ERROR out of range hex escape
    let z = "\xe2"; //~ ERROR out of range hex escape
    let a = b"\x00e2";  // ok because byte literal
}


