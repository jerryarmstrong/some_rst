tests/ui/feature-gates/stable-features.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Testing that the stable_features lint catches use of stable
// language and lib features.

#![deny(stable_features)]

#![feature(test_accepted_feature)]
//~^ ERROR the feature `test_accepted_feature` has been stable since 1.0.0

#![feature(rust1)]
//~^ ERROR the feature `rust1` has been stable since 1.0.0

fn main() {
    let _foo: Vec<()> = Vec::new();
}


