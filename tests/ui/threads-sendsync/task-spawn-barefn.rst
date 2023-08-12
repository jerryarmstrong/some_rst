tests/ui/threads-sendsync/task-spawn-barefn.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-fail
// error-pattern:Ensure that the child thread runs by panicking
// ignore-emscripten Needs threads.

use std::thread;

fn main() {
    // the purpose of this test is to make sure that thread::spawn()
    // works when provided with a bare function:
    let r = thread::spawn(startfn).join();
    if r.is_err() {
        panic!()
    }
}

fn startfn() {
    assert!("Ensure that the child thread runs by panicking".is_empty());
}


