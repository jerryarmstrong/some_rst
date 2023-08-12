tests/ui/drop/auxiliary/inline_dtor.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="inline_dtor"]

pub struct Foo;

impl Drop for Foo {
    #[inline]
    fn drop(&mut self) {}
}


