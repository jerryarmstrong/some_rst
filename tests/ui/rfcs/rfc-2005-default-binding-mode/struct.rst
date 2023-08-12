tests/ui/rfcs/rfc-2005-default-binding-mode/struct.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#[derive(Debug, PartialEq)]
struct Foo {
    x: u8,
}

pub fn main() {
    let mut foo = Foo {
        x: 1,
    };

    match &mut foo {
        Foo{x: n} => {
            *n += 1;
        },
    };

    assert_eq!(foo, Foo{x: 2});

    let Foo{x: n} = &foo;
    assert_eq!(*n, 2);
}


