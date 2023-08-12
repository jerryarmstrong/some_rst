src/tools/clippy/tests/ui-cargo/multiple_crate_versions/fail/src/main.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --crate-name=multiple_crate_versions
#![warn(clippy::multiple_crate_versions)]

fn main() {}


