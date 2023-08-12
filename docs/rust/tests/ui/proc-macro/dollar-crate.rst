tests/ui/proc-macro/dollar-crate.rs
===================================

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

mod local {
    macro_rules! local {
        () => {
            print_bang! {
                struct M($crate::S);
            }

            #[print_attr]
            struct A($crate::S);

            #[derive(Print)]
            struct D($crate::S);
        };
    }

    local!();
}

mod external {
    use crate::dollar_crate_external;

    dollar_crate_external::external!();
}

fn main() {}


