tests/ui/parser/removed-syntax-field-let.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    let foo: (),
    //~^  ERROR expected identifier, found keyword `let`
}

fn main() {}


