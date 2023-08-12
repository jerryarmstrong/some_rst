tests/rustdoc/auxiliary/rustdoc-default-impl.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]

pub mod bar {
    use std::marker;

    pub auto trait Bar {}

    pub trait Foo {
        fn foo(&self) {}
    }

    impl Foo {
        pub fn test<T: Bar>(&self) {}
    }

    pub struct TypeId;

    impl TypeId {
        pub fn of<T: Bar + ?Sized>() -> TypeId {
            panic!()
        }
    }
}


