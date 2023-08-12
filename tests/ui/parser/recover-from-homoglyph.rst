tests/ui/parser/recover-from-homoglyph.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!(""); //~ ERROR unknown start of token: \u{37e}
    let x: usize = (); //~ ERROR mismatched types
}


