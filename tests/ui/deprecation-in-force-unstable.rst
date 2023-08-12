tests/ui/deprecation-in-force-unstable.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:-Zforce-unstable-if-unmarked

#[deprecated] // should work even with -Zforce-unstable-if-unmarked
fn main() { }


