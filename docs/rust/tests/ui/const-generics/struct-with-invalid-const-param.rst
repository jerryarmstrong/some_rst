tests/ui/const-generics/struct-with-invalid-const-param.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks that a const param cannot be stored in a struct.

struct S<const C: u8>(C); //~ ERROR expected type, found const parameter

fn main() {}


