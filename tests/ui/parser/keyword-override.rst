tests/ui/parser/keyword-override.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let override = (); //~ ERROR expected identifier, found reserved keyword `override`
}


