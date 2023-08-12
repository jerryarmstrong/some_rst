src/tools/clippy/tests/ui/missing_inline_executable.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::missing_inline_in_public_items)]

pub fn foo() {}

fn main() {}


