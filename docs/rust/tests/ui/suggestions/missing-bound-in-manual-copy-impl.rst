tests/ui/suggestions/missing-bound-in-manual-copy-impl.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#[derive(Clone)]
struct Wrapper<T>(T);

impl<S> Copy for Wrapper<S> {}
//~^ ERROR the trait `Copy` may not be implemented for this type

fn main() {}


