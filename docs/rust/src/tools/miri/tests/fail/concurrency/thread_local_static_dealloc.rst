src/tools/miri/tests/fail/concurrency/thread_local_static_dealloc.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Ensure that thread-local statics get deallocated when the thread dies.

#![feature(thread_local)]

#[thread_local]
static mut TLS: u8 = 0;

struct SendRaw(*const u8);
unsafe impl Send for SendRaw {}

fn main() {
    unsafe {
        let dangling_ptr = std::thread::spawn(|| SendRaw(&TLS as *const u8)).join().unwrap();
        let _val = *dangling_ptr.0; //~ ERROR: dereferenced after this allocation got freed
    }
}


