src/tools/miri/tests/fail/dangling_pointers/maybe_null_pointer_deref_zst.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Some optimizations remove ZST accesses, thus masking this UB.
//@compile-flags: -Zmir-opt-level=0

fn main() {
    // This pointer *could* be NULL so we cannot load from it, not even at ZST
    let ptr = (&0u8 as *const u8).wrapping_sub(0x800) as *const ();
    let _x: () = unsafe { *ptr }; //~ ERROR: out-of-bounds
}


