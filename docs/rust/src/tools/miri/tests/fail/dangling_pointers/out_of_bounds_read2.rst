src/tools/miri/tests/fail/dangling_pointers/out_of_bounds_read2.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let v: Vec<u8> = vec![1, 2];
    let x = unsafe { *v.as_ptr().wrapping_offset(5) }; //~ ERROR: out-of-bounds
    panic!("this should never print: {}", x);
}


