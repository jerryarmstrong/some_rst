tests/ui/structs-enums/enum-export-inheritance.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

mod a {
    pub enum Foo {
        Bar,
        Baz,
        Boo
    }
}

pub fn main() {
    let _x = a::Foo::Bar;
}


