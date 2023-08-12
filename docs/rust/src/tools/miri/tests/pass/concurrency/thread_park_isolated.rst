src/tools/miri/tests/pass/concurrency/thread_park_isolated.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@ignore-target-apple: park_timeout on macOS uses the system clock
use std::thread;
use std::time::{Duration, Instant};

fn main() {
    let start = Instant::now();

    thread::park_timeout(Duration::from_millis(200));

    // Thanks to deterministic execution, this will wiat *exactly* 200ms (rounded to 1ms).
    assert!((200..201).contains(&start.elapsed().as_millis()));
}


