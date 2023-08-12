tests/ui/rfcs/rfc-2005-default-binding-mode/box.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unreachable_patterns)]
#![feature(box_patterns)]

struct Foo{}

pub fn main() {
    let b = Box::new(Foo{});
    let box f = &b;
    let _: &Foo = f;

    match &&&b {
        box f => {
            let _: &Foo = f;
        },
        _ => panic!(),
    }
}


