tests/ui/macros/macro-with-braces-in-expr-position.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_must_use)]
// ignore-emscripten no threads support

use std::thread;

macro_rules! expr { ($e: expr) => { $e } }

macro_rules! spawn {
    ($($code: tt)*) => {
        expr!(thread::spawn(move|| {$($code)*}).join())
    }
}

pub fn main() {
    spawn! {
        println!("stmt");
    };
    let _ = spawn! {
        println!("expr");
    };
}


