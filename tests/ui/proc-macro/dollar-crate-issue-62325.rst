tests/ui/proc-macro/dollar-crate-issue-62325.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018
// compile-flags: -Z span-debug
// aux-build:test-macros.rs
// aux-build:dollar-crate-external.rs


#![no_std] // Don't load unnecessary hygiene information from std
extern crate std;

#[macro_use]
extern crate test_macros;
extern crate dollar_crate_external;

type S = u8;

macro_rules! m { () => {
    #[print_attr]
    struct A(identity!($crate::S));
}}

m!();

dollar_crate_external::issue_62325!();

fn main() {}


