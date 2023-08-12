src/tools/miri/tests/fail/unaligned_pointers/unaligned_ptr_zst.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This should fail even without validation
// Some optimizations remove ZST accesses, thus masking this UB.
//@compile-flags: -Zmir-opt-level=0 -Zmiri-disable-validation

fn main() {
    // Try many times as this might work by chance.
    for i in 0..20 {
        let x = i as u8;
        let x = &x as *const _ as *const [u32; 0];
        // This must fail because alignment is violated. Test specifically for loading ZST.
        let _x = unsafe { *x }; //~ERROR: alignment 4 is required
    }
}


