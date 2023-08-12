tests/ui/parser/doc-comment-in-if-statement.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    if true /*!*/ {}
    //~^ ERROR outer attributes are not allowed on
    //~| ERROR expected outer doc comment
}


