tests/ui/cfg/crt-static-off-works.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(stable_features)]
// compile-flags:-C target-feature=-crt-static -Z unstable-options
// ignore-musl - requires changing the linker which is hard

#![feature(cfg_target_feature)]

#[cfg(not(target_feature = "crt-static"))]
fn main() {}


