tests/rustdoc/duplicate_impls/impls.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo;

// just so that `Foo` doesn't show up on `Bar`s sidebar
pub mod bar {
    pub trait Bar {}
}

impl Foo {
    pub fn new() -> Foo { Foo }
}

impl bar::Bar for Foo {}


