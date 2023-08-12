tests/ui/parser/keyword-ref-as-identifier.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let ref = "foo"; //~ error: expected identifier, found `=`
}


