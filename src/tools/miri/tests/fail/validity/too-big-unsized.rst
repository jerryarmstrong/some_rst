src/tools/miri/tests/fail/validity/too-big-unsized.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem;

#[allow(unused)]
struct MySlice {
    prefix: u64,
    tail: [u8],
}

fn main() {
    unsafe {
        let ptr = Box::into_raw(Box::new(0u8));
        // The slice part is actually not "too big", but together with the `prefix` field it is.
        let _x: &MySlice = mem::transmute((ptr, isize::MAX as usize)); //~ ERROR: invalid reference metadata: total size is bigger than largest supported object
    }
}


