tests/ui/unique/unique-destructure.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(box_patterns)]

struct Foo { a: isize, b: isize }

pub fn main() {
    let box Foo{ a, b } = Box::new(Foo { a: 100, b: 200 });
    assert_eq!(a + b, 300);
}


