tests/rustdoc/return-impl-trait.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(type_alias_impl_trait)]

pub trait Backend {}

impl Backend for () {}

pub struct Module<T>(T);

pub type BackendImpl = impl Backend;

// @has return_impl_trait/fn.make_module.html
/// Documentation
pub fn make_module() -> Module<BackendImpl> {
    Module(())
}


