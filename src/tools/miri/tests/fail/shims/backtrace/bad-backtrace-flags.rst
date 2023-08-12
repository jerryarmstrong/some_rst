src/tools/miri/tests/fail/shims/backtrace/bad-backtrace-flags.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "Rust" {
    fn miri_get_backtrace(flags: u64, buf: *mut *mut ());
}

fn main() {
    unsafe {
        miri_get_backtrace(2, std::ptr::null_mut()); //~ ERROR:  unsupported operation: unknown `miri_get_backtrace` flags 2
    }
}


