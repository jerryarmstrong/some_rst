tests/ui/proc-macro/dollar-crate-issue-57089.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018
// compile-flags: -Z span-debug
// aux-build:test-macros.rs

#![no_std] // Don't load unnecessary hygiene information from std
extern crate std;

#[macro_use]
extern crate test_macros;

type S = u8;

macro_rules! m {
    () => {
        print_bang! {
            struct M($crate::S);
        }

        #[print_attr]
        struct A($crate::S);
    };
}

m!();

fn main() {}


