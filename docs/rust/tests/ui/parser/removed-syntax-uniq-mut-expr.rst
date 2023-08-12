tests/ui/parser/removed-syntax-uniq-mut-expr.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a_box = box mut 42; //~ ERROR expected expression, found keyword `mut`
}


