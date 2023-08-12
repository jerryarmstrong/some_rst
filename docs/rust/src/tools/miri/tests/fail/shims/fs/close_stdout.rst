src/tools/miri/tests/fail/shims/fs/close_stdout.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows
//@compile-flags: -Zmiri-disable-isolation

// FIXME: standard handles cannot be closed (https://github.com/rust-lang/rust/issues/40032)

fn main() {
    unsafe {
        libc::close(1); //~ ERROR: cannot close stdout
    }
}


