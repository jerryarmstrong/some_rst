tests/ui/parser/doc-after-struct-field.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct X {
    a: u8 /** document a */,
    //~^ ERROR found a documentation comment that doesn't document anything
    //~| HELP if a comment was intended use `//`
}

struct Y {
    a: u8 /// document a
    //~^ ERROR found a documentation comment that doesn't document anything
    //~| HELP if a comment was intended use `//`
}

fn main() {
    let x = X { a: 1 };
    let y = Y { a: 1 };
}


