src/tools/miri/tests/fail/concurrency/windows_join_detached.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@only-target-windows: Uses win32 api functions
//@error-pattern: Undefined Behavior: trying to join a detached thread

// Joining a detached thread is undefined behavior.

use std::os::windows::io::{AsRawHandle, RawHandle};
use std::thread;

extern "system" {
    fn CloseHandle(handle: RawHandle) -> u32;
}

fn main() {
    let thread = thread::spawn(|| ());

    unsafe {
        assert_ne!(CloseHandle(thread.as_raw_handle()), 0);
    }

    thread.join().unwrap();
}


