tests/ui/unsized/unsized-inherent-impl-self-type.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test sized-ness checking in substitution in impls.

// impl - struct

struct S5<Y>(Y);

impl<X: ?Sized> S5<X> {
    //~^ ERROR the size for values of type
}

fn main() { }


