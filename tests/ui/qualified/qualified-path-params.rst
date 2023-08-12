tests/ui/qualified/qualified-path-params.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that qualified paths with type parameters
// fail during type checking and not during parsing

struct S;

trait Tr {
    type A;
}

impl Tr for S {
    type A = S;
}

impl S {
    fn f<T>() {}
}

fn main() {
    match 10 {
        <S as Tr>::A::f::<u8> => {}
        //~^ ERROR expected unit struct, unit variant or constant, found associated function
        0 ..= <S as Tr>::A::f::<u8> => {}
        //~^ ERROR only `char` and numeric types are allowed in range
    }
}


