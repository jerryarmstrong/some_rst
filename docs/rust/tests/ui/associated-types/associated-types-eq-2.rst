tests/ui/associated-types/associated-types-eq-2.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test equality constraints on associated types. Check we get an error when an
// equality constraint is used in a qualified path.

pub trait Foo {
    type A;
    fn boo(&self) -> <Self as Foo>::A;
}

struct Bar;

impl Foo for isize {
    type A = usize;
    fn boo(&self) -> usize { 42 }
}

fn baz<I: Foo>(x: &<I as Foo<A=Bar>>::A) {}
//~^ ERROR associated type bindings are not allowed here

pub fn main() {}


