tests/mir-opt/remove_storage_markers.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: RemoveStorageMarkers

// Checks that storage markers are removed at opt-level=0.
//
// compile-flags: -C opt-level=0 -Coverflow-checks=off

// EMIT_MIR remove_storage_markers.main.RemoveStorageMarkers.diff
fn main() {
    let mut sum = 0;
    for i in 0..10 {
        sum += i;
    }
}


