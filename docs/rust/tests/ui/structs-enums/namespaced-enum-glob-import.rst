tests/ui/structs-enums/namespaced-enum-glob-import.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

mod m2 {
    pub enum Foo {
        A,
        B(isize),
        C { a: isize },
    }

    impl Foo {
        pub fn foo() {}
    }
}

mod m {
    pub use m2::Foo::*;
}

fn _f(f: m2::Foo) {
    use m2::Foo::*;

    match f {
        A | B(_) | C { .. } => {}
    }
}

fn _f2(f: m2::Foo) {
    match f {
        m::A | m::B(_) | m::C { .. } => {}
    }
}

pub fn main() {}


