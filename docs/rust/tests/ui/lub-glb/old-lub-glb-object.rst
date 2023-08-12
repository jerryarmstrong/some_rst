tests/ui/lub-glb/old-lub-glb-object.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we give a note when the old LUB/GLB algorithm would have
// succeeded but the new code (which is stricter) gives an error.

trait Foo<T, U> {}

fn foo(x: &dyn for<'a, 'b> Foo<&'a u8, &'b u8>, y: &dyn for<'a> Foo<&'a u8, &'a u8>) {
    let z = match 22 {
        0 => x,
        _ => y,
        //~^ ERROR mismatched types
        //~| ERROR mismatched types
    };
}

fn bar(x: &dyn for<'a, 'b> Foo<&'a u8, &'b u8>, y: &dyn for<'a> Foo<&'a u8, &'a u8>) {
    // Accepted with explicit case:
    let z = match 22 {
        0 => x as &dyn for<'a> Foo<&'a u8, &'a u8>,
        _ => y,
    };
}

fn main() {}


