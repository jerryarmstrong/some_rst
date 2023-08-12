tests/ui/type/auxiliary/crate_a1.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo;

pub trait Bar{}

pub fn bar() -> Box<Bar> {
    unimplemented!()
}


pub fn try_foo(x: Foo){}
pub fn try_bar(x: Box<Bar>){}


