tests/rustdoc/inline_cross/auxiliary/rustdoc-trait-object-impl.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt;

pub trait Bar {}

impl<'a> Bar + 'a {
    pub fn bar(&self) -> usize { 42 }
}

impl<'a> fmt::Debug for Bar + 'a {
    fn fmt(&self, _: &mut fmt::Formatter) -> fmt::Result {
        Ok(())
    }
}


