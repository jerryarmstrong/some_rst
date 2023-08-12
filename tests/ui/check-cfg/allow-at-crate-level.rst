tests/ui/check-cfg/allow-at-crate-level.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test check that #![allow(unexpected_cfgs)] works with --cfg
//
// check-pass
// compile-flags: --cfg=unexpected --check-cfg=names() -Z unstable-options

#![allow(unexpected_cfgs)]

fn main() {}


