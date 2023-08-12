tests/ui/moves/moves-based-on-type-capture-clause.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
// ignore-emscripten no threads support

use std::thread;

pub fn main() {
    let x = "Hello world!".to_string();
    thread::spawn(move|| {
        println!("{}", x);
    }).join();
}


