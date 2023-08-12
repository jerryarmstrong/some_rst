tests/ui/feature-gates/feature-gate-allow-internal-unstable.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_macros)]

#[allow_internal_unstable()] //~ ERROR allow_internal_unstable side-steps
macro_rules! foo {
    () => {}
}

fn main() {}


