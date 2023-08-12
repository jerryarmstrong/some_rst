tests/ui/type-alias-impl-trait/auto-trait-leakage.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]
#![allow(dead_code)]

mod m {
    type Foo = impl std::fmt::Debug;

    pub fn foo() -> Foo {
        22_u32
    }
}

fn is_send<T: Send>(_: T) {}

fn main() {
    is_send(m::foo());
}


