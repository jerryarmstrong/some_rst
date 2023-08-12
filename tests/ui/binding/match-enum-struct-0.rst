tests/ui/binding/match-enum-struct-0.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// regression test for issue #5625


enum E {
    Foo{f : isize},
    Bar
}

pub fn main() {
    let e = E::Bar;
    match e {
        E::Foo{f: _f} => panic!(),
        _ => (),
    }
}


