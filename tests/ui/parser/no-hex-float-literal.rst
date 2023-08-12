tests/ui/parser/no-hex-float-literal.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    0xABC.Df;
    //~^ ERROR `{integer}` is a primitive type and therefore doesn't have fields
    0x567.89;
    //~^ ERROR hexadecimal float literal is not supported
    0xDEAD.BEEFp-2f;
    //~^ ERROR invalid suffix `f` for float literal
    //~| ERROR `{integer}` is a primitive type and therefore doesn't have fields
}


