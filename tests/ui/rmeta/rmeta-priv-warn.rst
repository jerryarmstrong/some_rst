tests/ui/rmeta/rmeta-priv-warn.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --emit=metadata
// no-prefer-dynamic
// build-pass (FIXME(62277): could be check-pass?)

#[deny(warnings)]

// Test that we don't get warnings for non-pub main when only emitting metadata.
// (#38273)

fn main() {
}


