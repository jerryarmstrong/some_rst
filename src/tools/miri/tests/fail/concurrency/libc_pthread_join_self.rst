src/tools/miri/tests/fail/concurrency/libc_pthread_join_self.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-windows: No libc on Windows
// We are making scheduler assumptions here.
//@compile-flags: -Zmiri-preemption-rate=0

// Joining itself is undefined behavior.

use std::{ptr, thread};

fn main() {
    let handle = thread::spawn(|| {
        unsafe {
            let native: libc::pthread_t = libc::pthread_self();
            assert_eq!(libc::pthread_join(native, ptr::null_mut()), 0); //~ ERROR: Undefined Behavior: trying to join itself
        }
    });
    thread::yield_now();
    handle.join().unwrap();
}


