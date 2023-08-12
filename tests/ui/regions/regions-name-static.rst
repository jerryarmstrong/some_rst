tests/ui/regions/regions-name-static.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<'static> {
    //~^ ERROR invalid lifetime parameter name: `'static`
    x: &'static isize,
}

fn main() {}


