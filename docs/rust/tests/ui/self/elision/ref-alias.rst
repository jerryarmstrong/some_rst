tests/ui/self/elision/ref-alias.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![allow(non_snake_case)]

use std::pin::Pin;

struct Struct { }

type Alias = Struct;

impl Struct {
    // Test using an alias for `Struct`:
    //
    // FIXME. We currently fail to recognize this as the self type, which
    // feels like a bug.

    fn ref_Alias(self: &Alias, f: &u32) -> &u32 {
        f
    }

    fn box_ref_Alias(self: Box<&Alias>, f: &u32) -> &u32 {
        f
    }

    fn pin_ref_Alias(self: Pin<&Alias>, f: &u32) -> &u32 {
        f
    }

    fn box_box_ref_Alias(self: Box<Box<&Alias>>, f: &u32) -> &u32 {
        f
    }

    fn box_pin_ref_Alias(self: Box<Pin<&Alias>>, f: &u32) -> &u32 {
        f
    }
}

fn main() { }


