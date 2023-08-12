tests/ui/traits/alias/import.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(trait_alias)]

mod inner {
    pub trait Foo {
        fn foo(&self);
    }

    pub struct Qux;

    impl Foo for Qux {
        fn foo(&self) {}
    }

    pub trait Bar = Foo;
}

mod two {
    pub trait A {
        fn foo();
    }

    impl A for u8 {
        fn foo() {}
    }
}

// Import only the alias, not the `Foo` trait.
use inner::{Bar, Qux};

// Declaring an alias also brings in aliased methods.
trait Two = two::A;

fn main() {
    let q = Qux;
    q.foo(); // From Bar.

    u8::foo(); // From A.
}


