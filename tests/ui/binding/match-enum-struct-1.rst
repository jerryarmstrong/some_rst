tests/ui/binding/match-enum-struct-1.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

enum E {
    Foo{f : isize},
    Bar
}

pub fn main() {
    let e = E::Foo{f: 1};
    match e {
        E::Foo{..} => (),
        _ => panic!(),
    }
    match e {
        E::Foo{f: _f} => (),
        _ => panic!(),
    }
}


