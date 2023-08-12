tests/ui-fulldeps/macro-crate-rlib.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:rlib-crate-test.rs
// ignore-cross-compile gives a different error message

#![feature(plugin)]
#![plugin(rlib_crate_test)]
//~^ ERROR: plugin `rlib_crate_test` only found in rlib format, but must be available in dylib

fn main() {}


