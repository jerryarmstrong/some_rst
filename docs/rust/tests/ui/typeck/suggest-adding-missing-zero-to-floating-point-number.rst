tests/ui/typeck/suggest-adding-missing-zero-to-floating-point-number.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    2.e1; //~ERROR `{integer}` is a primitive type and therefore doesn't have fields
    2.E1; //~ERROR `{integer}` is a primitive type and therefore doesn't have fields
    2.f32; //~ERROR `{integer}` is a primitive type and therefore doesn't have fields
    2.f64; //~ERROR `{integer}` is a primitive type and therefore doesn't have fields
    2.e+12; //~ERROR `{integer}` is a primitive type and therefore doesn't have fields
    2.e-12; //~ERROR `{integer}` is a primitive type and therefore doesn't have fields
    2.e1f32; //~ERROR `{integer}` is a primitive type and therefore doesn't have fields
}


