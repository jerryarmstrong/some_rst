tests/ui/parser/byte-string-literals.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static FOO: &'static [u8] = b"\f";  //~ ERROR unknown byte escape

pub fn main() {
    b"\f";  //~ ERROR unknown byte escape
    b"\x0Z";  //~ ERROR invalid character in numeric character escape: `Z`
    b"é";  //~ ERROR non-ASCII character in byte string literal
    br##"é"##;  //~ ERROR non-ASCII character in raw byte string literal
    b"a  //~ ERROR unterminated double quote byte string
}


