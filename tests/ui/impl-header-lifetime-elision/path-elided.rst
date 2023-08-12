tests/ui/impl-header-lifetime-elision/path-elided.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(warnings)]

trait MyTrait { }

struct Foo<'a> { x: &'a u32 }

impl MyTrait for Foo {
    //~^ ERROR implicit elided lifetime not allowed here
}

fn main() {}


