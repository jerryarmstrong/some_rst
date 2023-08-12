tests/ui/tydesc-name.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]

use std::any::type_name;

struct Foo<T> {
    x: T
}

pub fn main() {
    assert_eq!(type_name::<isize>(), "isize");
    assert_eq!(type_name::<Foo<usize>>(), "tydesc_name::Foo<usize>");
}


