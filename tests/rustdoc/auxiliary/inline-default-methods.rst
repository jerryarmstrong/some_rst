tests/rustdoc/auxiliary/inline-default-methods.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Cmetadata=aux

pub trait Foo {
    fn bar(&self);
    fn foo(&mut self) {}
}


