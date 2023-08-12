src/tools/miri/tests/fail/validity/too-big-slice.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem;

fn main() {
    unsafe {
        let ptr = Box::into_raw(Box::new(0u8));
        let _x: &[u8] = mem::transmute((ptr, usize::MAX)); //~ ERROR: invalid reference metadata: slice is bigger than largest supported object
    }
}


