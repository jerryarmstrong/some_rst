tests/ui/array-slice-vec/slice-2.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that slicing syntax gives errors if we have not implemented the trait.

struct Foo;

fn main() {
    let x = Foo;
    &x[..]; //~ ERROR cannot index into a value of type `Foo`
    &x[Foo..]; //~ ERROR cannot index into a value of type `Foo`
    &x[..Foo]; //~ ERROR cannot index into a value of type `Foo`
    &x[Foo..Foo]; //~ ERROR cannot index into a value of type `Foo`
}


