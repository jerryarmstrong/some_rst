tests/ui/traits/bound/auxiliary/crate_a2.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo;

pub trait Bar {}

impl Bar for Foo {}

pub struct DoesNotImplementTrait;

pub struct ImplementsWrongTraitConditionally<T> {
    _marker: std::marker::PhantomData<T>,
}

impl Bar for ImplementsWrongTraitConditionally<isize> {}


