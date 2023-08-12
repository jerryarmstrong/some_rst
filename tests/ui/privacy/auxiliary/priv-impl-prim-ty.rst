tests/ui/privacy/auxiliary/priv-impl-prim-ty.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait A {
    fn frob(&self);
}

impl A for isize { fn frob(&self) {} }

pub fn frob<T:A>(t: T) {
    t.frob();
}


