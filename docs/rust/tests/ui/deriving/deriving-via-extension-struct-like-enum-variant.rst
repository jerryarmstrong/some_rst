tests/ui/deriving/deriving-via-extension-struct-like-enum-variant.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#[derive(PartialEq, Debug)]
enum S {
    X { x: isize, y: isize },
    Y
}

pub fn main() {
    let x = S::X { x: 1, y: 2 };
    assert_eq!(x, x);
    assert!(!(x != x));
}


