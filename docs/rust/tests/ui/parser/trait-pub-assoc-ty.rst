tests/ui/parser/trait-pub-assoc-ty.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    pub type Foo;
    //~^ ERROR unnecessary visibility qualifier
}

fn main() {}


