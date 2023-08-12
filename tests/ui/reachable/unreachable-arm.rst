tests/ui/reachable/unreachable-arm.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_patterns)]

#![allow(dead_code)]
#![deny(unreachable_patterns)]

enum Foo { A(Box<Foo>, isize), B(usize), }

fn main() {
    match Foo::B(1) {
        Foo::B(_) | Foo::A(box _, 1) => { }
        Foo::A(_, 1) => { } //~ ERROR unreachable pattern
        _ => { }
    }
}


