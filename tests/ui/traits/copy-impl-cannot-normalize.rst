tests/ui/traits/copy-impl-cannot-normalize.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait TraitFoo {
    type Bar;
}

struct Foo<T>
where
    T: TraitFoo,
{
    inner: T::Bar,
}

impl<T> Clone for Foo<T>
where
    T: TraitFoo,
    T::Bar: Clone,
{
    fn clone(&self) -> Self {
        Self { inner: self.inner.clone() }
    }
}

impl<T> Copy for Foo<T> {}
//~^ ERROR the trait bound `T: TraitFoo` is not satisfied

fn main() {}


