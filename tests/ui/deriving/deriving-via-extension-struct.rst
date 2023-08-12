tests/ui/deriving/deriving-via-extension-struct.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#[derive(PartialEq, Debug)]
struct Foo {
    x: isize,
    y: isize,
    z: isize,
}

pub fn main() {
    let a = Foo { x: 1, y: 2, z: 3 };
    let b = Foo { x: 1, y: 2, z: 3 };
    assert_eq!(a, b);
    assert!(!(a != b));
    assert!(a.eq(&b));
    assert!(!a.ne(&b));
}


