tests/rustdoc/auxiliary/issue-27362-aux.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Cmetadata=aux

pub const fn foo() {}
pub const unsafe fn bar() {}

pub struct Foo;

impl Foo {
    pub const unsafe fn baz() {}
}


