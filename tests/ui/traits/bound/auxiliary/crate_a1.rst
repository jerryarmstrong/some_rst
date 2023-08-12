tests/ui/traits/bound/auxiliary/crate_a1.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Bar {}

pub fn try_foo(x: impl Bar) {}

pub struct ImplementsTraitForUsize<T> {
    _marker: std::marker::PhantomData<T>,
}

impl Bar for ImplementsTraitForUsize<usize> {}


