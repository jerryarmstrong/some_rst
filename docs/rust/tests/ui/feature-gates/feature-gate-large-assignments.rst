tests/ui/feature-gates/feature-gate-large-assignments.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check that `move_size_limit is feature-gated

#![move_size_limit = "42"] //~ ERROR the `#[move_size_limit]` attribute is an experimental feature

fn main() {}


