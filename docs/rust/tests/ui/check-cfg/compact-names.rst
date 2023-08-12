tests/ui/check-cfg/compact-names.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test check that we correctly emit an warning for compact cfg
//
// check-pass
// compile-flags:--check-cfg=names() -Z unstable-options

#![feature(cfg_target_compact)]

#[cfg(target(os = "linux", arch = "arm"))]
pub fn expected() {}

#[cfg(target(os = "linux", architecture = "arm"))]
//~^ WARNING unexpected `cfg` condition name
pub fn unexpected() {}

fn main() {}


