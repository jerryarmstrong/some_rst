src/tools/miri/tests/pass/concurrency/mutex_leak.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-ignore-leaks
use std::mem;
use std::sync::Mutex;

fn main() {
    // Test for https://github.com/rust-lang/rust/issues/85434
    let m = Mutex::new(5i32);
    mem::forget(m.lock());
}


