tests/rustdoc/trait-self-link.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has trait_self_link/trait.Foo.html //a/@href trait.Foo.html
pub trait Foo {}

pub struct Bar;

impl Foo for Bar {}


