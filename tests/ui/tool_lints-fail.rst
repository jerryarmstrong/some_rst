tests/ui/tool_lints-fail.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Don't allow tool_lints, which aren't scoped


#![deny(unknown_lints)]

#![deny(clippy)] //~ ERROR: unknown lint: `clippy`

fn main() {}


