tests/ui/impl-trait/in-trait/auxiliary/rpitit.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(return_position_impl_trait_in_trait)]

pub trait Foo {
    fn bar() -> impl Sized;
}

pub struct Foreign;

impl Foo for Foreign {
    fn bar() {}
}


