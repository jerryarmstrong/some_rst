tests/ui-fulldeps/missing-rustc-driver-error.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we get the following hint when trying to use a compiler crate without rustc_driver.
// error-pattern: try adding `extern crate rustc_driver;` at the top level of this crate
// compile-flags: --emit link
// The exactly list of required crates depends on the target. as such only test Unix targets.
// only-unix

#![feature(rustc_private)]

extern crate rustc_serialize;

fn main() {}


