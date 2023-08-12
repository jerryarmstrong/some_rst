tests/ui/self/elision/ref-mut-alias.rs
======================================

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

    fn ref_Alias(self: &mut Alias, f: &u32) -> &u32 {
        f
    }

    fn box_ref_Alias(self: Box<&mut Alias>, f: &u32) -> &u32 {
        f
    }

    fn pin_ref_Alias(self: Pin<&mut Alias>, f: &u32) -> &u32 {
        f
    }

    fn box_box_ref_Alias(self: Box<Box<&mut Alias>>, f: &u32) -> &u32 {
        f
    }

    fn box_pin_ref_Alias(self: Box<Pin<&mut Alias>>, f: &u32) -> &u32 {
        f
    }
}

fn main() { }


