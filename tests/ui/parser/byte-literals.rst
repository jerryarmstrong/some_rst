tests/ui/parser/byte-literals.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-tab

static FOO: u8 = b'\f';  //~ ERROR unknown byte escape

pub fn main() {
    b'\f';  //~ ERROR unknown byte escape
    b'\x0Z';  //~ ERROR invalid character in numeric character escape: `Z`
    b'	';  //~ ERROR byte constant must be escaped
    b''';  //~ ERROR byte constant must be escaped
    b'é';  //~ ERROR non-ASCII character in byte literal
    b'a  //~ ERROR unterminated byte constant [E0763]
}


