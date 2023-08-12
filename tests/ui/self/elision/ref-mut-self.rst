tests/ui/self/elision/ref-mut-self.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(non_snake_case)]

use std::pin::Pin;

struct Struct { }

impl Struct {
    // Test using `&mut self` sugar:

    fn ref_self(&mut self, f: &u32) -> &u32 {
        f
        //~^ ERROR lifetime may not live long enough
    }

    // Test using `&mut Self` explicitly:

    fn ref_Self(self: &mut Self, f: &u32) -> &u32 {
        f
        //~^ ERROR lifetime may not live long enough
    }

    fn box_ref_Self(self: Box<&mut Self>, f: &u32) -> &u32 {
        f
        //~^ ERROR lifetime may not live long enough
    }

    fn pin_ref_Self(self: Pin<&mut Self>, f: &u32) -> &u32 {
        f
        //~^ ERROR lifetime may not live long enough
    }

    fn box_box_ref_Self(self: Box<Box<&mut Self>>, f: &u32) -> &u32 {
        f
        //~^ ERROR lifetime may not live long enough
    }

    fn box_pin_ref_Self(self: Box<Pin<&mut Self>>, f: &u32) -> &u32 {
        f
        //~^ ERROR lifetime may not live long enough
    }
}

fn main() { }


