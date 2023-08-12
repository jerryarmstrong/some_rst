tests/ui/parser/raw/raw-byte-string-literals.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-cr

pub fn main() {
    br"a"; //~ ERROR bare CR not allowed in raw string
    br"é";  //~ ERROR non-ASCII character in raw byte string literal
    br##~"a"~##;  //~ ERROR only `#` is allowed in raw string delimitation
}


