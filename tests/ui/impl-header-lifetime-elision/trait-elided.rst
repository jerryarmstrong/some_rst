tests/ui/impl-header-lifetime-elision/trait-elided.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]

trait MyTrait<'a> {}

impl MyTrait for u32 {}
//~^ ERROR implicit elided lifetime not allowed here

fn main() {}


