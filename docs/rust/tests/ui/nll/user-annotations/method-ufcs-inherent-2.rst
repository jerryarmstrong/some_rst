tests/ui/nll/user-annotations/method-ufcs-inherent-2.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that substitutions given on the self type (here, `A`) can be
// used in combination with annotations given for method arguments.

struct A<'a> { x: &'a u32 }

impl<'a> A<'a> {
    fn new<'b, T>(x: &'a u32, y: T) -> Self {
        Self { x }
    }
}

fn foo<'a>() {
    let v = 22;
    let x = A::<'a>::new::<&'a u32>(&v, &v);
    //~^ ERROR
    //~| ERROR
}

fn main() {}


