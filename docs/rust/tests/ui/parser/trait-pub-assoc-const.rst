tests/ui/parser/trait-pub-assoc-const.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    pub const Foo: u32;
    //~^ ERROR unnecessary visibility qualifier
}

fn main() {}


