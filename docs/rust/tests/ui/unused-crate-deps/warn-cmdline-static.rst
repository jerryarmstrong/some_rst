tests/ui/unused-crate-deps/warn-cmdline-static.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check for unused crate dep, no path

// edition:2018
// check-pass
// compile-flags: -Wunused-crate-dependencies
// aux-crate:bar=bar.rs
// no-prefer-dynamic

fn main() {}
//~^ WARNING external crate `bar` unused in


