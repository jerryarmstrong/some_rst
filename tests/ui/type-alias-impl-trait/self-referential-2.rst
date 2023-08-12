tests/ui/type-alias-impl-trait/self-referential-2.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl std::fmt::Debug;
type Bar = impl PartialEq<Foo>;

fn bar() -> Bar {
    42_i32 //~^ ERROR can't compare `i32` with `Foo`
}

fn main() {}


