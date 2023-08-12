tests/ui/issues/auxiliary/issue-9155.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo<T>(T);

impl<T> Foo<T> {
    pub fn new(t: T) -> Foo<T> {
        Foo(t)
    }
}


