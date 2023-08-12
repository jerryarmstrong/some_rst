tests/ui/deprecation/derive_on_deprecated_forbidden.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#![forbid(deprecated)]

#[deprecated = "oh no"]
#[derive(Default)]
struct X;

fn main() {}


