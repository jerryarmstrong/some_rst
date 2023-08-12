tests/ui/deriving/deriving-via-extension-enum.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#[derive(PartialEq, Debug)]
enum Foo {
    Bar(isize, isize),
    Baz(f64, f64)
}

pub fn main() {
    let a = Foo::Bar(1, 2);
    let b = Foo::Bar(1, 2);
    assert_eq!(a, b);
    assert!(!(a != b));
    assert!(a.eq(&b));
    assert!(!a.ne(&b));
}


