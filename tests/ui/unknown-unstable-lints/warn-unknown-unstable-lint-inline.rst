tests/ui/unknown-unstable-lints/warn-unknown-unstable-lint-inline.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![warn(unknown_lints)]
#![allow(test_unstable_lint)]
//~^ WARNING unknown lint: `test_unstable_lint`
//~| WARNING unknown lint: `test_unstable_lint`
//~| WARNING unknown lint: `test_unstable_lint`

fn main() {}


