tests/ui/for-loop-while/for-loop-goofiness.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

enum BogusOption<T> {
    None,
    Some(T),
}

type Iterator = isize;

pub fn main() {
    let x = [ 3, 3, 3 ];
    for i in &x {
        assert_eq!(*i, 3);
    }
}


