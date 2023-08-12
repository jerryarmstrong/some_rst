tests/ui/parser/underscore-suffix-for-float.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a = 42._; //~ ERROR expected identifier, found reserved identifier `_`
                  //~| ERROR `{integer}` is a primitive type and therefore doesn't have fields
}


