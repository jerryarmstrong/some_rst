tests/ui/feature-gates/feature-gate-test_unstable_lint.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// `test_unstable_lint` is for testing and should never be stabilized.
#![allow(test_unstable_lint)]
//~^ WARNING unknown lint: `test_unstable_lint`
//~| WARNING unknown lint: `test_unstable_lint`
//~| WARNING unknown lint: `test_unstable_lint`

fn main() {}


