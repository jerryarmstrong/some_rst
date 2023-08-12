src/tools/miri/tests/fail/intrinsics/copy_null.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]

// Directly call intrinsic to avoid debug assertions in libstd
extern "rust-intrinsic" {
    fn copy_nonoverlapping<T>(src: *const T, dst: *mut T, count: usize);
}

fn main() {
    let mut data = [0u16; 4];
    let ptr = &mut data[0] as *mut u16;
    // Even copying 0 elements from NULL should error.
    unsafe {
        copy_nonoverlapping(std::ptr::null(), ptr, 0); //~ ERROR: memory access failed: null pointer is a dangling pointer
    }
}


