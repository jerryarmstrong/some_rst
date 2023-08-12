src/tools/miri/tests/pass/option_box_transmute_ptr.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This tests that the size of Option<Box<i32>> is the same as *const i32.
fn option_box_deref() -> i32 {
    let val = Some(Box::new(42));
    unsafe {
        let ptr: *const i32 = std::mem::transmute::<Option<Box<i32>>, *const i32>(val);
        let ret = *ptr;
        // unleak memory
        std::mem::transmute::<*const i32, Option<Box<i32>>>(ptr);
        ret
    }
}

fn main() {
    assert_eq!(option_box_deref(), 42);
}


