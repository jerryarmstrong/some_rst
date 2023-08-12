tests/ui/suggestions/auxiliary/meow.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Meow {
    fn meow(&self) {}
}

pub struct GlobalMeow;

impl Meow for GlobalMeow {}

pub(crate) struct PrivateMeow;

impl Meow for PrivateMeow {}


