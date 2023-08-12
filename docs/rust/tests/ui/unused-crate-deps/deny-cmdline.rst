tests/ui/unused-crate-deps/deny-cmdline.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check for unused crate dep, deny, expect failure

// edition:2018
// compile-flags: -Dunused-crate-dependencies
// aux-crate:bar=bar.rs

fn main() {}
//~^ ERROR external crate `bar` unused in


