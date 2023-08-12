tests/ui/cross-crate/const-cross-crate-extern.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:cci_const.rs
#![allow(non_upper_case_globals)]

extern crate cci_const;
use cci_const::bar;
static foo: extern "C" fn() = bar;

pub fn main() {
    assert!(foo == bar);
}


