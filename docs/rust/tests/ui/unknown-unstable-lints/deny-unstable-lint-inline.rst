tests/ui/unknown-unstable-lints/deny-unstable-lint-inline.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

#![deny(unknown_lints)]
#![allow(test_unstable_lint)]
//~^ ERROR unknown lint: `test_unstable_lint`
//~| ERROR unknown lint: `test_unstable_lint`
//~| ERROR unknown lint: `test_unstable_lint`

fn main() {}


