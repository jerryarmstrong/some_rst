tests/ui/feature-gates/feature-gate-lint-reasons.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(nonstandard_style, reason = "the standard should be respected")]
//~^ ERROR lint reasons are experimental
//~| ERROR lint reasons are experimental

fn main() {}


