tests/ui/issues/auxiliary/issue-7178.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo<'a, A:'a>(&'a A);

impl<'a, A> Foo<'a, A> {
    pub fn new(a: &'a A) -> Foo<'a, A> {
        Foo(a)
    }
}


