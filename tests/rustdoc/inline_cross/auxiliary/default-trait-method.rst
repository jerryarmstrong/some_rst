tests/rustdoc/inline_cross/auxiliary/default-trait-method.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(specialization)]

#![crate_name = "foo"]

pub trait Item {
    fn foo();
    fn bar();
    fn baz() {}
}

pub struct Foo;

impl Item for Foo {
    default fn foo() {}
    fn bar() {}
}


