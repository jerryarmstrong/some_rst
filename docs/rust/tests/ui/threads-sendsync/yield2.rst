tests/ui/threads-sendsync/yield2.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::thread;

pub fn main() {
    let mut i: isize = 0;
    while i < 100 { i = i + 1; println!("{}", i); thread::yield_now(); }
}


