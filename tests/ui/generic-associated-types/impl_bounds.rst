tests/ui/generic-associated-types/impl_bounds.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(associated_type_defaults)]

trait Foo {
    type A<'a> where Self: 'a;
    type B<'a, 'b> where 'a: 'b;
    type C where Self: Clone;
    fn d() where Self: Clone;
}

#[derive(Copy, Clone)]
struct Fooy<T>(T);

impl<T> Foo for Fooy<T> {
    type A<'a> = (&'a ()) where Self: 'static;
    //~^ ERROR impl has stricter requirements than trait
    type B<'a, 'b> = (&'a(), &'b ()) where 'b: 'a;
    //~^ ERROR impl has stricter requirements than trait
    type C = String where Self: Copy;
    //~^ ERROR the trait bound `T: Copy` is not satisfied
    fn d() where Self: Copy {}
    //~^ ERROR the trait bound `T: Copy` is not satisfied
}

fn main() {}


