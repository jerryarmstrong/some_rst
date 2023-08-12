tests/ui/type/type-params-in-different-spaces-3.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Tr : Sized {
    fn test<X>(u: X) -> Self {
        u   //~ ERROR mismatched types
    }
}

fn main() {}


