tests/ui/type-alias-impl-trait/incomplete-inference.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl Sized;

fn bar() -> Foo {
    None
    //~^ ERROR: type annotations needed [E0282]
}

fn baz() -> Foo {
    Some(())
}

fn main() {}


