src/tools/clippy/tests/ui/blanket_clippy_restriction_lints.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -W clippy::restriction

#![warn(clippy::blanket_clippy_restriction_lints)]

//! Test that the whole restriction group is not enabled
#![warn(clippy::restriction)]
#![deny(clippy::restriction)]
#![forbid(clippy::restriction)]

fn main() {}


