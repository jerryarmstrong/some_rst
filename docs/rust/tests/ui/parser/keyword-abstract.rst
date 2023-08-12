tests/ui/parser/keyword-abstract.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let abstract = (); //~ ERROR expected identifier, found reserved keyword `abstract`
}


