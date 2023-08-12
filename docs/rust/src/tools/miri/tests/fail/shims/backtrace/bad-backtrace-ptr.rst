src/tools/miri/tests/fail/shims/backtrace/bad-backtrace-ptr.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "Rust" {
    fn miri_resolve_frame(ptr: *mut (), flags: u64);
}

fn main() {
    unsafe {
        miri_resolve_frame(std::ptr::null_mut(), 0); //~ ERROR: null pointer is a dangling pointer
    }
}


