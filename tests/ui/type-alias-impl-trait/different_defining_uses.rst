tests/ui/type-alias-impl-trait/different_defining_uses.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

fn main() {}

// two definitions with different types
type Foo = impl std::fmt::Debug;

fn foo() -> Foo {
    ""
}

fn bar() -> Foo {
    42i32
    //~^ ERROR concrete type differs from previous
}


