src/tools/miri/tests/fail/unaligned_pointers/unaligned_ptr2.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This should fail even without validation or Stacked Borrows.
//@compile-flags: -Zmiri-disable-validation -Zmiri-disable-stacked-borrows

fn main() {
    // No retry needed, this fails reliably.

    let x = [2u32, 3]; // Make it big enough so we don't get an out-of-bounds error.
    let x = (x.as_ptr() as *const u8).wrapping_offset(3) as *const u32;
    // This must fail because alignment is violated: the offset is not sufficiently aligned.
    // Also make the offset not a power of 2, that used to ICE.
    let _x = unsafe { *x }; //~ERROR: memory with alignment 1, but alignment 4 is required
}


