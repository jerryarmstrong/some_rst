tests/ui/issues/auxiliary/issue-2472-b.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct S(pub ());

impl S {
    pub fn foo(&self) { }
}

pub trait T {
    fn bar(&self);
}

impl T for S {
    fn bar(&self) { }
}


