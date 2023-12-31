src/tools/miri/tests/fail/data_race/dangling_thread_async_race.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // We want to control preemption here. Stacked borrows interferes by having its own accesses.
//@compile-flags: -Zmiri-preemption-rate=0 -Zmiri-disable-stacked-borrows

use std::mem;
use std::thread::{sleep, spawn};
use std::time::Duration;

#[derive(Copy, Clone)]
struct EvilSend<T>(pub T);

unsafe impl<T> Send for EvilSend<T> {}
unsafe impl<T> Sync for EvilSend<T> {}

fn main() {
    let mut a = 0u32;
    let b = &mut a as *mut u32;
    let c = EvilSend(b);

    let join = unsafe {
        spawn(move || {
            *c.0 = 32;
        })
    };

    // Detach the thread and sleep until it terminates
    mem::drop(join);
    sleep(Duration::from_millis(200));

    // Spawn and immediately join a thread
    // to execute the join code-path
    // and ensure that data-race detection
    // remains enabled nevertheless.
    spawn(|| ()).join().unwrap();

    let join2 = unsafe {
        spawn(move || {
            *c.0 = 64; //~ ERROR: Data race detected between (1) Write on thread `<unnamed>` and (2) Write on thread `<unnamed>`
        })
    };

    join2.join().unwrap();
}


