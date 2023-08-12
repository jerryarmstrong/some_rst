tests/ui/last-use-is-capture.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// Make sure #1399 stays fixed

struct A { a: Box<isize> }

pub fn main() {
    fn invoke<F>(f: F) where F: FnOnce() { f(); }
    let k: Box<_> = 22.into();
    let _u = A {a: k.clone()};
    invoke(|| println!("{}", k.clone()) )
}


