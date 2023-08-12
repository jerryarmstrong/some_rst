tests/ui/mir/mir_boxing.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(box_syntax)]

fn test() -> Box<i32> {
    box 42
}

fn main() {
    assert_eq!(*test(), 42);
}


