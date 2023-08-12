tests/ui/derives/derive-on-trait-item-or-impl-item.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    #[derive(Clone)]
    //~^ ERROR `derive` may only be applied to `struct`s, `enum`s and `union`s
    type Bar;
}

struct Bar;

impl Bar {
    #[derive(Clone)]
    //~^ ERROR `derive` may only be applied to `struct`s, `enum`s and `union`s
    fn bar(&self) {}
}

fn main() {}


