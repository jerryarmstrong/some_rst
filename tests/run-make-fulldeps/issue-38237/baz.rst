tests/run-make-fulldeps/issue-38237/baz.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate foo;
extern crate bar;

pub struct Bar;
impl ::std::ops::Deref for Bar {
    type Target = bar::S;
    fn deref(&self) -> &Self::Target { unimplemented!() }
}


