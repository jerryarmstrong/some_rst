tests/ui/stability-attribute/stability-attribute-sanity-3.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // More checks that stability attributes are used correctly

#![feature(staged_api)]

#![stable(feature = "stable_test_feature", since = "1.0.0")]

#[macro_export]
macro_rules! mac { //~ ERROR macro has missing stability attribute
    () => ()
}

fn main() { }


