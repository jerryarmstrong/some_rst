tests/ui/consts/const_in_pattern/cross-crate-fail.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:consts.rs

#![warn(indirect_structural_match)]

extern crate consts;

struct Defaulted;
impl consts::AssocConst for Defaulted {}

fn main() {
    let _ = Defaulted;
    match None {
        consts::SOME => panic!(),
        //~^ must be annotated with `#[derive(PartialEq, Eq)]`

        _ => {}
    }

    match None {
        <Defaulted as consts::AssocConst>::SOME  => panic!(),
        //~^ must be annotated with `#[derive(PartialEq, Eq)]`

        _ => {}
    }
}


