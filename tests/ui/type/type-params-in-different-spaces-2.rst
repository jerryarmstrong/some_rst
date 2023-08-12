tests/ui/type/type-params-in-different-spaces-2.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test static calls to make sure that we align the Self and input
// type parameters on a trait correctly.

trait Tr<T> : Sized {
    fn op(_: T) -> Self;
}

trait A:    Tr<Self> {
    fn test<U>(u: U) -> Self {
        Tr::op(u)   //~ ERROR E0277
    }
}

trait B<T>: Tr<T> {
    fn test<U>(u: U) -> Self {
        Tr::op(u)   //~ ERROR E0277
    }
}

fn main() {
}


