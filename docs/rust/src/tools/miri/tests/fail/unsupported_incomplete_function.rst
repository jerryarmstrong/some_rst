src/tools/miri/tests/fail/unsupported_incomplete_function.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! `signal()` is special on Linux and macOS that it's only supported within libstd.
//! The implementation is not complete enough to permit user code to call it.
//@ignore-target-windows: No libc on Windows
//@normalize-stderr-test: "OS `.*`" -> "$$OS"

fn main() {
    unsafe {
        libc::signal(libc::SIGPIPE, libc::SIG_IGN);
        //~^ ERROR: unsupported operation: can't call foreign function `signal`
    }
}


