tests/ui/feature-gates/allow-features-empty.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z allow_features=
// Note: This test uses rustc internal flags because they will never stabilize.

#![feature(lang_items)] //~ ERROR

#![feature(unknown_stdlib_feature)] //~ ERROR

fn main() {}


