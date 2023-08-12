tests/ui/type-alias-impl-trait/cross_crate_ice2.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:cross_crate_ice2.rs
// build-pass (FIXME(62277): could be check-pass?)

extern crate cross_crate_ice2;

use cross_crate_ice2::View;

fn main() {
    let v = cross_crate_ice2::X;
    v.test();
}


