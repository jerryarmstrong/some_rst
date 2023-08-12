src/tools/miri/tests/fail/unaligned_pointers/unaligned_ptr1.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This should fail even without validation or Stacked Borrows.
//@compile-flags: -Zmiri-disable-validation -Zmiri-disable-stacked-borrows

fn main() {
    // Try many times as this might work by chance.
    for _ in 0..20 {
        let x = [2u16, 3, 4]; // Make it big enough so we don't get an out-of-bounds error.
        let x = &x[0] as *const _ as *const u32;
        // This must fail because alignment is violated: the allocation's base is not sufficiently aligned.
        let _x = unsafe { *x }; //~ERROR: memory with alignment 2, but alignment 4 is required
    }
}


