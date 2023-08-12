tests/ui/traits/alias/auxiliary/greeter.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(trait_alias)]

pub trait Hello {
    fn hello(&self);
}

pub struct Hi;

impl Hello for Hi {
    fn hello(&self) {}
}

pub trait Greet = Hello;


