tests/ui/feature-gates/issue-43106-gating-of-macro_escape.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Testing that crate-level `#![macro_escape]` is not gated beyond a
// depecation warning.  This file sits on its own, because crate-level
// `#![macro_escape]` is incompatible with crate-level `#![macro_use]`
// already present in issue-43106-gating-of-builtin-attrs.

// check-pass

#![macro_escape]
//~^ WARN `#[macro_escape]` is a deprecated synonym for `#[macro_use]`

fn main() {}


