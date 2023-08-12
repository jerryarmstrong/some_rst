src/tools/miri/tests/fail/intrinsics/ptr_offset_overflow.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v = [1i8, 2];
    let x = &v[1] as *const i8;
    let _val = unsafe { x.offset(isize::MIN) }; //~ERROR: overflowing in-bounds pointer arithmetic
}


