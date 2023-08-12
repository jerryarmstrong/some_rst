tests/ui/const-generics/defaults/default-annotation.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(staged_api)]
#![allow(incomplete_features)]
// FIXME(const_generics_defaults): It seems like we aren't testing the right thing here,
// I would assume that we want the attributes to apply to the const parameter defaults
// themselves.
#![stable(feature = "const_default_test", since="none")]

#[unstable(feature = "const_default_stable", issue="none")]
pub struct ConstDefaultUnstable<const N: usize = 3>;

#[stable(feature = "const_default_unstable", since="none")]
pub struct ConstDefaultStable<const N: usize = {
    3
}>;

fn main() {}


