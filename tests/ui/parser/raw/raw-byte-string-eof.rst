tests/ui/parser/raw/raw-byte-string-eof.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn main() {
    br##"a"#;  //~ unterminated raw string
}


