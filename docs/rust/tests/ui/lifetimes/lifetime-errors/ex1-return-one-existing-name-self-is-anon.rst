tests/ui/lifetimes/lifetime-errors/ex1-return-one-existing-name-self-is-anon.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    field: i32,
}

impl Foo {
    fn foo<'a>(&self, x: &'a Foo) -> &'a Foo {

        if true { x } else { self }
        //~^ ERROR lifetime may not live long enough

    }
}

fn main() {}


