tests/ui/cfg/cfg-match-arm.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

enum Foo {
    Bar,
    Baz,
}

fn foo(f: Foo) {
    match f {
        Foo::Bar => {},
        #[cfg(not(asdfa))]
        Foo::Baz => {},
        #[cfg(afsd)]
        Basdfwe => {}
    }
}

pub fn main() {}


