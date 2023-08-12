tests/ui/drop/drop-trait.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
struct Foo {
    x: isize
}

impl Drop for Foo {
    fn drop(&mut self) {
        println!("bye");
    }
}

pub fn main() {
    let _x: Foo = Foo { x: 3 };
}


