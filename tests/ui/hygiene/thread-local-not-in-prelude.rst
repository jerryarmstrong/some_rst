tests/ui/hygiene/thread-local-not-in-prelude.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![no_std]

extern crate std;

std::thread_local!(static A: usize = 30);

fn main() {
}


