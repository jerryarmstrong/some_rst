src/tools/miri/tests/fail/intrinsics/out_of_bounds_ptr_2.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v = [0i8; 4];
    let x = &v as *const i8;
    let x = unsafe { x.offset(isize::MIN) }; //~ERROR: overflowing in-bounds pointer arithmetic
    panic!("this should never print: {:?}", x);
}


