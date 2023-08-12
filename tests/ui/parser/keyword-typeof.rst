tests/ui/parser/keyword-typeof.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let typeof = (); //~ ERROR expected identifier, found reserved keyword `typeof`
}


