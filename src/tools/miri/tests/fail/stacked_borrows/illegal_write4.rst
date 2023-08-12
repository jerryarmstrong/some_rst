src/tools/miri/tests/fail/stacked_borrows/illegal_write4.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem;

fn main() {
    let mut target = 42;
    // Make sure we cannot use a raw-tagged `&mut` pointing to a frozen location.
    // Even just creating it unfreezes.
    let raw = &mut target as *mut _; // let this leak to raw
    let reference = unsafe { &*raw }; // freeze
    let _ptr = reference as *const _ as *mut i32; // raw ptr, with raw tag
    let _mut_ref: &mut i32 = unsafe { mem::transmute(raw) }; // &mut, with raw tag
    // Now we retag, making our ref top-of-stack -- and, in particular, unfreezing.
    let _val = *reference; //~ ERROR: /read access .* tag does not exist in the borrow stack/
}


