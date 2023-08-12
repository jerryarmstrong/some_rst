src/tools/clippy/tests/ui/empty_enum_without_never_type.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]
#![warn(clippy::empty_enum)]

// `never_type` is not enabled; this test has no stderr file
enum Empty {}

fn main() {}


