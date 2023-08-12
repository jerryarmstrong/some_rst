src/tools/clippy/tests/ui-cargo/feature_name/fail/src/main.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-name=feature_name
#![warn(clippy::redundant_feature_names)]
#![warn(clippy::negative_feature_names)]

fn main() {
    // test code goes here
}


