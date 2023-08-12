tests/ui/conditional-compilation/auxiliary/namespaced_enums.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum Foo {
    A,
    B(isize),
    C { a: isize },
}

impl Foo {
    pub fn foo() {}
    pub fn bar(&self) {}
}


