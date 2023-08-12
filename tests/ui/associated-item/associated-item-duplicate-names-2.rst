tests/ui/associated-item/associated-item-duplicate-names-2.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;

impl Foo {
    const bar: bool = true;
    fn bar() {} //~ ERROR duplicate definitions
}

fn main() {}


