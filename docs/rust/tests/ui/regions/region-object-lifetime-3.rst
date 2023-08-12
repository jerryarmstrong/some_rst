tests/ui/regions/region-object-lifetime-3.rs
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

// Borrowed receiver with two distinct lifetimes, but we know that
// 'b:'a, hence &'a () is permitted.
fn borrowed_receiver_related_lifetimes<'a,'b>(x: &'a (Foo+'b)) -> &'a () {
    x.borrowed()
}


fn main() {}


