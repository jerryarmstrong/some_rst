tests/ui/type-alias-impl-trait/nested.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

type Foo = impl std::fmt::Debug;
type Bar = impl Trait<Foo>;

trait Trait<T> {}

impl<T, U> Trait<T> for U {}

fn bar() -> Bar {
    42
}

fn main() {
    println!("{:?}", bar());
    //~^ ERROR `Bar` doesn't implement `Debug`
}


