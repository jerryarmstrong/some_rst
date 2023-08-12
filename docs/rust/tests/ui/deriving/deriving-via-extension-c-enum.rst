tests/ui/deriving/deriving-via-extension-c-enum.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#[derive(PartialEq, Debug)]
enum Foo {
    Bar,
    Baz,
    Boo
}

pub fn main() {
    let a = Foo::Bar;
    let b = Foo::Bar;
    assert_eq!(a, b);
    assert!(!(a != b));
    assert!(a.eq(&b));
    assert!(!a.ne(&b));
}


