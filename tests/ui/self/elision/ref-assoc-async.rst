tests/ui/self/elision/ref-assoc-async.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// check-pass

#![allow(non_snake_case)]

use std::pin::Pin;

trait Trait {
    type AssocType;
}

struct Struct { }

impl Trait for Struct {
    type AssocType = Self;
}

impl Struct {
    async fn ref_AssocType(self: &<Struct as Trait>::AssocType, f: &u32) -> &u32 {
        f
    }

    async fn box_ref_AssocType(self: Box<&<Struct as Trait>::AssocType>, f: &u32) -> &u32 {
        f
    }

    async fn pin_ref_AssocType(self: Pin<&<Struct as Trait>::AssocType>, f: &u32) -> &u32 {
        f
    }

    async fn box_box_ref_AssocType(self: Box<Box<&<Struct as Trait>::AssocType>>, f: &u32) -> &u32 {
        f
    }

    async fn box_pin_ref_AssocType(self: Box<Pin<&<Struct as Trait>::AssocType>>, f: &u32) -> &u32 {
        f
    }
}

fn main() { }


