tests/ui/suggestions/use-type-argument-instead-of-assoc-type.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub trait T<X, Y> {
    type A;
    type B;
    type C;
}
pub struct Foo {
    i: Box<dyn T<usize, usize, usize, usize, B=usize>>,
    //~^ ERROR must be specified
    //~| ERROR this trait takes 2 generic arguments but 4 generic arguments were supplied
}


fn main() {}


