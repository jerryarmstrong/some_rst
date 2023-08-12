tests/ui/generics/generic-unique.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

struct Triple<T> { x: T, y: T, z: T }

fn box_it<T>(x: Triple<T>) -> Box<Triple<T>> { return Box::new(x); }

pub fn main() {
    let x: Box<Triple<isize>> = box_it::<isize>(Triple{x: 1, y: 2, z: 3});
    assert_eq!(x.y, 2);
}


