tests/ui/parser/doc-before-struct-rbrace-1.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct X {
    a: u8,
    /// document
    //~^ ERROR found a documentation comment that doesn't document anything
    //~| HELP if a comment was intended use `//`
}

fn main() {
    let y = X {a: 1};
}


