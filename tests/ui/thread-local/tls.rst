tests/ui/thread-local/tls.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-emscripten no threads support
// compile-flags: -O

#![feature(thread_local)]

#[thread_local]
static S: u32 = 222;

fn main() {
    let local = &S as *const u32 as usize;
    let foreign = std::thread::spawn(|| &S as *const u32 as usize).join().unwrap();
    assert_ne!(local, foreign);
}


