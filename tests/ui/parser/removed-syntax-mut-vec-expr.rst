tests/ui/parser/removed-syntax-mut-vec-expr.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v = [mut 1, 2, 3, 4]; //~ ERROR expected expression, found keyword `mut`
}


