src/tools/miri/tests/fail/intrinsics/out_of_bounds_ptr_1.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v = [0i8; 4];
    let x = &v as *const i8;
    // The error is inside another function, so we cannot match it by line
    let x = unsafe { x.offset(5) }; //~ERROR: pointer to 5 bytes starting at offset 0 is out-of-bounds
    panic!("this should never print: {:?}", x);
}


