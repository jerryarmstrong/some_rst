tests/ui/type-alias-impl-trait/type-alias-impl-trait-with-cycle-error2.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

pub trait Bar<T> {
    type Item;
}

type Foo = impl Bar<Foo, Item = Foo>;
//~^ ERROR: unconstrained opaque type

fn crash(x: Foo) -> Foo {
    x
}

fn main() {}


