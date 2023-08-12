src/tools/miri/tests/fail/intrinsics/write_bytes_null.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]

// Directly call intrinsic to avoid debug assertions in libstd
extern "rust-intrinsic" {
    fn write_bytes<T>(dst: *mut T, val: u8, count: usize);
}

fn main() {
    unsafe { write_bytes::<u8>(std::ptr::null_mut(), 0, 0) }; //~ ERROR: memory access failed: null pointer is a dangling pointer
}


