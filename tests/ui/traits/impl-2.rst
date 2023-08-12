tests/ui/traits/impl-2.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_snake_case)]

// pretty-expanded FIXME #23616

pub mod Foo {
    pub trait Trait {
        fn foo(&self);
    }
}

mod Bar {
    impl<'a> dyn (::Foo::Trait) + 'a {
        fn bar(&self) { self.foo() }
    }
}

fn main() {}


