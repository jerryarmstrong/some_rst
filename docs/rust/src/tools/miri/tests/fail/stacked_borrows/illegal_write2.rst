src/tools/miri/tests/fail/stacked_borrows/illegal_write2.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let target = &mut 42;
    let target2 = target as *mut _;
    drop(&mut *target); // reborrow
    // Now make sure our ref is still the only one.
    unsafe { *target2 = 13 }; //~ ERROR: /write access .* tag does not exist in the borrow stack/
    let _val = *target;
}


