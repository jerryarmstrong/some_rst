tests/ui/impl-trait/fallback_inference.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::marker::PhantomData;

fn weird() -> PhantomData<impl Sized> {
    PhantomData //~ ERROR type annotations needed
}

fn main() {}


