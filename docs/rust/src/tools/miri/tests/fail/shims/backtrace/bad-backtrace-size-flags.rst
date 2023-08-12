src/tools/miri/tests/fail/shims/backtrace/bad-backtrace-size-flags.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "Rust" {
    fn miri_backtrace_size(flags: u64) -> usize;
}

fn main() {
    unsafe {
        miri_backtrace_size(2); //~ ERROR:  unsupported operation: unknown `miri_backtrace_size` flags 2
    }
}


