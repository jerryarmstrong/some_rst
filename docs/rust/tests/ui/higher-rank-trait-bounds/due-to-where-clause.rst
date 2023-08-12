tests/ui/higher-rank-trait-bounds/due-to-where-clause.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    test::<FooS>(&mut 42); //~ ERROR implementation of `Foo` is not general enough
}

trait Foo<'a> {}

struct FooS<'a> {
    data: &'a mut u32,
}

impl<'a, 'b: 'a> Foo<'b> for FooS<'a> {}

fn test<'a, F>(data: &'a mut u32) where F: for<'b> Foo<'b> {}


