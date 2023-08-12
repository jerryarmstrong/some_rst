tests/ui/regions/region-object-lifetime-5.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Various tests related to testing how region inference works
// with respect to the object receivers.

trait Foo {
    fn borrowed<'a>(&'a self) -> &'a ();
}

// Here, the object is bounded by an anonymous lifetime and returned
// as `&'static`, so you get an error.
fn owned_receiver(x: Box<dyn Foo>) -> &'static () {
    x.borrowed() //~ ERROR cannot return reference to local data `*x`
}

fn main() {}


