src/tools/miri/tests/pass/sendable-class.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a class with only sendable fields can be sent

use std::sync::mpsc::channel;

#[allow(dead_code)]
struct Foo {
    i: isize,
    j: char,
}

fn foo(i: isize, j: char) -> Foo {
    Foo { i: i, j: j }
}

pub fn main() {
    let (tx, rx) = channel();
    tx.send(foo(42, 'c')).unwrap();
    let _val = rx;
}


