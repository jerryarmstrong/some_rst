tests/ui/regions/region-object-lifetime-2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Various tests related to testing how region inference works
// with respect to the object receivers.

trait Foo {
    fn borrowed<'a>(&'a self) -> &'a ();
}

// Borrowed receiver but two distinct lifetimes, we get an error.
fn borrowed_receiver_different_lifetimes<'a,'b>(x: &'a dyn Foo) -> &'b () {
    x.borrowed()
    //~^ ERROR lifetime may not live long enough
}

fn main() {}


