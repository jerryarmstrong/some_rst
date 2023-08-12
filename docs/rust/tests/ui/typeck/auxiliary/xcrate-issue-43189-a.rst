tests/ui/typeck/auxiliary/xcrate-issue-43189-a.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]


pub trait A {
    fn a(&self) {}
}
impl A for () {}


