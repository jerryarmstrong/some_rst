tests/ui/regions/region-object-lifetime-1.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Various tests related to testing how region inference works
// with respect to the object receivers.

// check-pass
#![allow(warnings)]

trait Foo {
    fn borrowed<'a>(&'a self) -> &'a ();
}

// Here the receiver and return value all have the same lifetime,
// so no error results.
fn borrowed_receiver_same_lifetime<'a>(x: &'a Foo) -> &'a () {
    x.borrowed()
}


fn main() {}


