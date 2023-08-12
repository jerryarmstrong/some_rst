tests/ui/drop/drop-trait-generic.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
struct S<T> {
    x: T
}

impl<T> ::std::ops::Drop for S<T> {
    fn drop(&mut self) {
        println!("bye");
    }
}

pub fn main() {
    let _x = S { x: 1 };
}


