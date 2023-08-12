tests/ui/self/auxiliary/explicit_self_xcrate.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait Foo {
    #[inline(always)]
    fn f(&self);
}

pub struct Bar {
    pub x: String
}

impl Foo for Bar {
    #[inline(always)]
    fn f(&self) {
        println!("{}", (*self).x);
    }
}


