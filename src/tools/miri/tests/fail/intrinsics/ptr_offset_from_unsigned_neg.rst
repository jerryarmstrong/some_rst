src/tools/miri/tests/fail/intrinsics/ptr_offset_from_unsigned_neg.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(ptr_sub_ptr)]

fn main() {
    let arr = [0u8; 8];
    let ptr1 = arr.as_ptr();
    let ptr2 = ptr1.wrapping_add(4);
    let _val = unsafe { ptr1.sub_ptr(ptr2) }; //~ERROR: first pointer has smaller offset than second: 0 < 4
}


