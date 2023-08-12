tests/ui/structs-enums/auxiliary/namespaced_enum_emulate_flat.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub use Foo::*;

pub enum Foo {
    A,
    B(isize),
    C { a: isize },
}

impl Foo {
    pub fn foo() {}
}

pub mod nest {
    pub use self::Bar::*;

    pub enum Bar {
        D,
        E(isize),
        F { a: isize },
    }

    impl Bar {
        pub fn foo() {}
    }
}


