tests/ui/parser/raw/raw-string.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = r##"lol"#;
    //~^ ERROR unterminated raw string
}


