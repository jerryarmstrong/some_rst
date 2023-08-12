src/tools/miri/tests/pass/track-alloc-1.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Ensure that tracking early allocations doesn't ICE Miri.
// Early allocations are probably part of the runtime and therefore uninteresting, but they
// shouldn't cause a crash.
//@compile-flags: -Zmiri-track-alloc-id=1
//@normalize-stderr-test: "[48] bytes" -> "SIZE bytes"
fn main() {}


