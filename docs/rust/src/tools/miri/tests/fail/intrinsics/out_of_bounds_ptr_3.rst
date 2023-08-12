src/tools/miri/tests/fail/intrinsics/out_of_bounds_ptr_3.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v = [0i8; 4];
    let x = &v as *const i8;
    let x = unsafe { x.offset(-1) }; //~ERROR: pointer to 1 byte starting at offset -1 is out-of-bounds
    panic!("this should never print: {:?}", x);
}


