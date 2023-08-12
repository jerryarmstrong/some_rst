tests/ui/variants/variant-used-as-type.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test error message when enum variants are used as types


// issue 21225
enum Ty {
    A,
    B(Ty::A),
    //~^ ERROR expected type, found variant `Ty::A`
}


// issue 19197
enum E {
    A
}

impl E::A {}
//~^ ERROR expected type, found variant `E::A`

fn main() {}


