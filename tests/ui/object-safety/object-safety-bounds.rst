tests/ui/object-safety/object-safety-bounds.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Traits with bounds mentioning `Self` are not object safe

trait X {
    type U: PartialEq<Self>;
}

fn f() -> Box<dyn X<U = u32>> {
    //~^ ERROR the trait `X` cannot be made into an object
    loop {}
}

fn main() {}


