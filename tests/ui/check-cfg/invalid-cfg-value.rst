tests/ui/check-cfg/invalid-cfg-value.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check warning for invalid configuration value
//
// edition:2018
// check-pass
// compile-flags: --check-cfg=values(feature,"serde","full") --cfg=feature="rand" -Z unstable-options

#[cfg(feature = "sedre")]
//~^ WARNING unexpected `cfg` condition value
pub fn f() {}

#[cfg(feature = "serde")]
pub fn g() {}

#[cfg(feature = "rand")]
//~^ WARNING unexpected `cfg` condition value
pub fn h() {}

pub fn main() {}


