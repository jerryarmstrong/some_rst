tests/ui/traits/auxiliary/traitimpl.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test inherent trait impls work cross-crait.

pub trait Bar<'a> : 'a {}

impl<'a> Bar<'a> {
    pub fn bar(&self) {}
}


