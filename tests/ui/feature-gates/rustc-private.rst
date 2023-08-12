tests/ui/feature-gates/rustc-private.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-rustc_private

extern crate libc; //~ ERROR  use of unstable library feature 'rustc_private'

fn main() {}


