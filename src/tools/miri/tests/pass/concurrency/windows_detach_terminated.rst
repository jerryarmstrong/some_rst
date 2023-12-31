src/tools/miri/tests/pass/concurrency/windows_detach_terminated.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@only-target-windows: Uses win32 api functions
// We are making scheduler assumptions here.
//@compile-flags: -Zmiri-preemption-rate=0

use std::os::windows::io::IntoRawHandle;
use std::thread;

extern "system" {
    fn CloseHandle(handle: usize) -> i32;
}

fn main() {
    let thread = thread::spawn(|| {}).into_raw_handle() as usize;

    // this yield ensures that `thread` is terminated by this point
    thread::yield_now();

    unsafe {
        assert_ne!(CloseHandle(thread), 0);
    }
}


