tests/ui/parser/doc-before-fn-rbrace.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    /// document
    //~^ ERROR found a documentation comment that doesn't document anything
    //~| HELP if a comment was intended use `//`
}


