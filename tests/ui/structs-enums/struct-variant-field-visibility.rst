tests/ui/structs-enums/struct-variant-field-visibility.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

mod foo {
    pub enum Foo {
        Bar { a: isize }
    }
}

fn f(f: foo::Foo) {
    match f {
        foo::Foo::Bar { a: _a } => {}
    }
}

pub fn main() {}


