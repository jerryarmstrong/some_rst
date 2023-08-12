tests/ui/issues/issue-44216-add-instant.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:overflow
// ignore-emscripten no processes

use std::time::{Instant, Duration};

fn main() {
    let now = Instant::now();
    let _ = now + Duration::from_secs(u64::MAX);
}


