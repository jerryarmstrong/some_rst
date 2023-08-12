tests/ui/issues/issue-44216-add-system-time.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:overflow
// ignore-emscripten no processes

use std::time::{Duration, SystemTime};

fn main() {
    let now = SystemTime::now();
    let _ = now + Duration::from_secs(u64::MAX);
}


