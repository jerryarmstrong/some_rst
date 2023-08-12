src/tools/miri/tests/panic/unsupported_syscall.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows
//@ignore-target-apple: `syscall` is not supported on macOS
//@compile-flags: -Zmiri-panic-on-unsupported

fn main() {
    unsafe {
        libc::syscall(0);
    }
}


