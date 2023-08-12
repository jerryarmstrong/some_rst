src/tools/miri/tests/fail/dangling_pointers/dangling_zst_deref.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure we find these even with many checks disabled.
// Some optimizations remove ZST accesses, thus masking this UB.
//@compile-flags: -Zmir-opt-level=0 -Zmiri-disable-alignment-check -Zmiri-disable-stacked-borrows -Zmiri-disable-validation

fn main() {
    let p = {
        let b = Box::new(42);
        &*b as *const i32 as *const ()
    };
    let _x = unsafe { *p }; //~ ERROR: dereferenced after this allocation got freed
}


