tests/run-make/track-path-dep-info/macro_use.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_use]
extern crate macro_def;

access_tracked_paths!();

fn main() {}


