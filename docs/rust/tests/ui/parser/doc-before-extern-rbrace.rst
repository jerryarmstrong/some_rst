tests/ui/parser/doc-before-extern-rbrace.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

extern "C" {
    /// hi
    //~^ ERROR found a documentation comment that doesn't document anything
}


