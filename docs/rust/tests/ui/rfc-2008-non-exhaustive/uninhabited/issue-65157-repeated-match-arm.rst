tests/ui/rfc-2008-non-exhaustive/uninhabited/issue-65157-repeated-match-arm.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:uninhabited.rs
#![deny(unreachable_patterns)]
#![feature(never_type)]

extern crate uninhabited;

use uninhabited::PartiallyInhabitedVariants;

// This test checks a redundant/useless pattern of a non-exhaustive enum/variant is still
// warned against.

pub fn foo(x: PartiallyInhabitedVariants) {
    match x {
        PartiallyInhabitedVariants::Struct { .. } => {},
        PartiallyInhabitedVariants::Struct { .. } => {},
        //~^ ERROR unreachable pattern
        _ => {},
    }
}

fn main() { }


