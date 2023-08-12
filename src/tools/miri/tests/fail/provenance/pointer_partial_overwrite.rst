src/tools/miri/tests/fail/provenance/pointer_partial_overwrite.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure we find these even with many checks disabled.
//@compile-flags: -Zmiri-disable-alignment-check -Zmiri-disable-stacked-borrows -Zmiri-disable-validation

// Test what happens when we overwrite parts of a pointer.

fn main() {
    let mut p = &42;
    unsafe {
        let ptr: *mut _ = &mut p;
        *(ptr as *mut u8) = 123; // this removes provenance from one of the bytes, meaning the entire ptr is considered to have no provenance.
    }
    let x = *p; //~ ERROR: no provenance
    panic!("this should never print: {}", x);
}


