tests/ui/deriving/deriving-default-box.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::default::Default;

#[derive(Default)]
struct A {
    foo: Box<[bool]>,
}

pub fn main() {
    let a: A = Default::default();
    let b: Box<[_]> = Box::<[bool; 0]>::new([]);
    assert_eq!(a.foo, b);
}


