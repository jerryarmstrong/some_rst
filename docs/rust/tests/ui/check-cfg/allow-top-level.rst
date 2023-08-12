tests/ui/check-cfg/allow-top-level.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test check that a top-level #![allow(unexpected_cfgs)] works
//
// check-pass
// compile-flags:--check-cfg=names() -Z unstable-options

#![allow(unexpected_cfgs)]

#[cfg(FALSE)]
fn bar() {}

fn foo() {
    if cfg!(FALSE) {}
}

fn main() {}


