tests/ui/parser/keyword-mut-as-identifier.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut = "foo"; //~ error: expected identifier, found `=`
}


