src/tools/miri/tests/fail/stacked_borrows/raw_tracking.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! This demonstrates a provenance problem that requires tracking of raw pointers to be detected.

fn main() {
    let mut l = 13;
    let raw1 = &mut l as *mut _;
    let raw2 = &mut l as *mut _; // invalidates raw1
    // Without raw pointer tracking, Stacked Borrows cannot distinguish raw1 and raw2, and thus
    // fails to realize that raw1 should not be used any more.
    unsafe { *raw1 = 13 }; //~ ERROR: /write access .* tag does not exist in the borrow stack/
    unsafe { *raw2 = 13 };
}


