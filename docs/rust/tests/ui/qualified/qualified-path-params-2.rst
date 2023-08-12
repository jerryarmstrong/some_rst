tests/ui/qualified/qualified-path-params-2.rs
=============================================

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

type A = <S as Tr>::A::f<u8>;
//~^ ERROR ambiguous associated type

fn main() {}


