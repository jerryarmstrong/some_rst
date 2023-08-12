tests/ui/associated-item/impl-duplicate-methods.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;

impl Foo {
    fn orange(&self) {}
    fn orange(&self) {}
    //~^ ERROR duplicate definitions with name `orange` [E0592]
}

fn main() {}


