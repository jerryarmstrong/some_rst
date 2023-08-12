tests/ui/issues/auxiliary/issue-8259.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum Foo<'a> {
    A,
    B(&'a str),
}


