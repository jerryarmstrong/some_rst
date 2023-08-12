tests/ui/enum-discriminant/forbidden-discriminant-kind-impl.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(discriminant_kind)]

use std::marker::DiscriminantKind;

enum Uninhabited {}

struct NewType;

impl DiscriminantKind for NewType {
    //~^ ERROR explicit impls for the `DiscriminantKind` trait are not permitted
    type Discriminant = Uninhabited;
}

fn main() {}


