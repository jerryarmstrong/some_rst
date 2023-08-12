tests/ui/traits/inheritance/auxiliary/xc_call.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Foo {
    fn f(&self) -> isize;
}

pub struct A {
    pub x: isize
}

impl Foo for A {
    fn f(&self) -> isize { 10 }
}


