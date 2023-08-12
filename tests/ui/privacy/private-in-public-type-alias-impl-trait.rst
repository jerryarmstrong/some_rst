tests/ui/privacy/private-in-public-type-alias-impl-trait.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![feature(type_alias_impl_trait)]
#![deny(private_in_public)]

pub type Pub = impl Default;

#[derive(Default)]
struct Priv;

fn check() -> Pub {
    Priv
}

pub trait Trait {
    type Pub: Default;
    fn method() -> Self::Pub;
}

impl Trait for u8 {
    type Pub = impl Default;
    fn method() -> Self::Pub {
        Priv
    }
}

fn main() {}


