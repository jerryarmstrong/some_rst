tests/ui/type/auxiliary/crate_a2.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo;

pub trait Bar{}

pub fn bar() -> Box<Bar> {
    unimplemented!()
}


