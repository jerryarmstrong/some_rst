tests/ui/impl-trait/recursive-type-alias-impl-trait-declaration-too-subtle-2.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl PartialEq<(Foo, i32)>;

struct Bar;

impl PartialEq<(Foo, i32)> for Bar {
    fn eq(&self, _other: &(Foo, i32)) -> bool {
        true
    }
}

fn foo() -> Foo {
    //~^ ERROR can't compare `Bar` with `(Bar, i32)`
    Bar
}

fn main() {}


