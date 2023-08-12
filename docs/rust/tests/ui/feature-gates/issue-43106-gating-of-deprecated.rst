tests/ui/feature-gates/issue-43106-gating-of-deprecated.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test just shows that a crate-level `#![deprecated]` does not
// signal a warning or error. (This file sits on its own because a
// crate-level `#![deprecated]` causes all that crate's item
// definitions to be deprecated, which is a pain to work with.)
//
// (For non-crate-level cases, see issue-43106-gating-of-builtin-attrs.rs)

// check-pass

#![deprecated]

fn main() {}


