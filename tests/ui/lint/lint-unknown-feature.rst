tests/ui/lint/lint-unknown-feature.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![warn(unused_features)]

#![allow(stable_features)]
// FIXME(#44232) we should warn that this isn't used.
#![feature(rust1)]

fn main() {}


