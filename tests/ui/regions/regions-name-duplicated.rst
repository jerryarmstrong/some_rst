tests/ui/regions/regions-name-duplicated.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<'a, 'a> {
    //~^ ERROR the name `'a` is already used for a generic parameter
    x: &'a isize,
}

fn main() {}


