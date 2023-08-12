tests/ui/rfcs/rfc-2005-default-binding-mode/tuple-struct.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
enum Foo {
    Bar(Option<i8>, (), (), Vec<i32>),
    Baz,
}

pub fn main() {
    let foo = Foo::Bar(Some(1), (), (), vec![2, 3]);

    match &foo {
        Foo::Baz => panic!(),
        Foo::Bar(None, ..) => panic!(),
        Foo::Bar(Some(n), .., v) => {
            assert_eq!((*v).len(), 2);
            assert_eq!(*n, 1);
        }
    }
}


