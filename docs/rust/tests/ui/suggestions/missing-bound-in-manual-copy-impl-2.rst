tests/ui/suggestions/missing-bound-in-manual-copy-impl-2.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#[derive(Clone)]
struct Wrapper<T>(T);

struct OnlyCopyIfDisplay<T>(std::marker::PhantomData<T>);

impl<T: std::fmt::Display> Clone for OnlyCopyIfDisplay<T> {
    fn clone(&self) -> Self {
        OnlyCopyIfDisplay(std::marker::PhantomData)
    }
}

impl<T: std::fmt::Display> Copy for OnlyCopyIfDisplay<T> {}

impl<S> Copy for Wrapper<OnlyCopyIfDisplay<S>> {}
//~^ ERROR the trait `Copy` may not be implemented for this type

fn main() {}


