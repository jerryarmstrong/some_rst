src/tools/clippy/tests/ui-internal/custom_ice_message.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustc-env:RUST_BACKTRACE=0
// normalize-stderr-test: "Clippy version: .*" -> "Clippy version: foo"
// normalize-stderr-test: "internal_lints.rs:\d*:\d*" -> "internal_lints.rs"
// normalize-stderr-test: "', .*clippy_lints" -> "', clippy_lints"
// normalize-stderr-test: "'rustc'" -> "'<unnamed>'"

#![deny(clippy::internal)]
#![allow(clippy::missing_clippy_version_attribute)]

fn it_looks_like_you_are_trying_to_kill_clippy() {}

fn main() {}


