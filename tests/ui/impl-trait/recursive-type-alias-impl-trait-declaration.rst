tests/ui/impl-trait/recursive-type-alias-impl-trait-declaration.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(type_alias_impl_trait)]

type Foo = impl PartialEq<(Foo, i32)>;

struct Bar;

impl PartialEq<(Bar, i32)> for Bar {
    fn eq(&self, _other: &(Bar, i32)) -> bool {
        true
    }
}

fn foo() -> Foo {
    Bar
}

fn main() {}


