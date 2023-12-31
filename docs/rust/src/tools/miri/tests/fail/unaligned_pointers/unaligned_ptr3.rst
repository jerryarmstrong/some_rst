src/tools/miri/tests/fail/unaligned_pointers/unaligned_ptr3.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This should fail even without validation or Stacked Borrows.
//@compile-flags: -Zmiri-disable-validation -Zmiri-disable-stacked-borrows

fn main() {
    // Try many times as this might work by chance.
    for _ in 0..20 {
        let x = [2u16, 3, 4, 5]; // Make it big enough so we don't get an out-of-bounds error.
        let x = &x[0] as *const _ as *const *const u8; // cast to ptr-to-ptr, so that we load a ptr
        // This must fail because alignment is violated. Test specifically for loading pointers,
        // which have special code in miri's memory.
        let _x = unsafe { *x }; //~ERROR: but alignment
    }
}


