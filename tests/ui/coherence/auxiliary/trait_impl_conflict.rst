tests/ui/coherence/auxiliary/trait_impl_conflict.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Foo {
    fn foo() {}
}

impl Foo for isize {
}


