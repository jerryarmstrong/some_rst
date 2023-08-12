tests/ui/privacy/useless-pub.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A { pub i: isize }

pub trait E {
    fn foo(&self);
}

impl E for A {
    pub fn foo(&self) {} //~ ERROR: unnecessary visibility qualifier
}

enum Foo {
    V1 { pub f: i32 }, //~ ERROR unnecessary visibility qualifier
    V2(pub i32), //~ ERROR unnecessary visibility qualifier
}

fn main() {}


