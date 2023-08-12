tests/ui/type-alias-impl-trait/defining-use-submodule.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]
#![allow(dead_code)]

// test that the type alias impl trait defining use is in a submodule

fn main() {}

type Foo = impl std::fmt::Display;
type Bar = impl std::fmt::Display;

mod foo {
    pub fn foo() -> super::Foo {
        "foo"
    }

    pub mod bar {
        pub fn bar() -> crate::Bar {
            1
        }
    }
}


