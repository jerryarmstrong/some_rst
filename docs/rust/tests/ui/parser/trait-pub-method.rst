tests/ui/parser/trait-pub-method.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    pub fn foo();
    //~^ ERROR unnecessary visibility qualifier
}

fn main() {}


