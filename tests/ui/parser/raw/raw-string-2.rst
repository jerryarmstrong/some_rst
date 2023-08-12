tests/ui/parser/raw/raw-string-2.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = r###"here's a long string"# "# "##;
    //~^ ERROR unterminated raw string
}


