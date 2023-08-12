tests/ui/lint/lint-unknown-feature-default.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// Tests the default for the unused_features lint

#![allow(stable_features)]
// FIXME(#44232) we should warn that this isn't used.
#![feature(rust1)]

fn main() {}


