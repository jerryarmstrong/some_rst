tests/ui/consts/const_in_pattern/cross-crate-pass.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:consts.rs

#![warn(indirect_structural_match)]

extern crate consts;
use consts::CustomEq;

struct Defaulted;
impl consts::AssocConst for Defaulted {}

fn main() {
    let _ = Defaulted;
    match Some(CustomEq) {
        consts::NONE => panic!(),
        _ => {}
    }

    match Some(CustomEq) {
        <Defaulted as consts::AssocConst>::NONE  => panic!(),
        _ => {}
    }
}


