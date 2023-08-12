tests/ui/deriving/deriving-via-extension-hash-enum.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#[derive(Hash)]
enum Foo {
    Bar(isize, char),
    Baz(char, isize)
}

#[derive(Hash)]
enum A {
    B,
    C,
    D,
    E
}

pub fn main(){}


