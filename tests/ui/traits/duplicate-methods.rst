tests/ui/traits/duplicate-methods.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn orange(&self);
    fn orange(&self); //~ ERROR the name `orange` is defined multiple times
}

fn main() {}


