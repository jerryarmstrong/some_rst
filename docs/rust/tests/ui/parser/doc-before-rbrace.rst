tests/ui/parser/doc-before-rbrace.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!("Hi"); /// hi
    //~^ ERROR found a documentation comment that doesn't document anything
    //~| HELP if a comment was intended use `//`
}


