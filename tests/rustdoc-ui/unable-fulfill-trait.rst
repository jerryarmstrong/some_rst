tests/rustdoc-ui/unable-fulfill-trait.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test ensures that it's not crashing rustdoc.

pub struct Foo<'a, 'b, T> {
    field1: dyn Bar<'a, 'b,>,
    //~^ ERROR
    //~^^ ERROR
}

pub trait Bar<'x, 's, U>
    where U: 'x,
    Self:'x,
    Self:'s
{}


