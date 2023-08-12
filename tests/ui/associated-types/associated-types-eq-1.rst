tests/ui/associated-types/associated-types-eq-1.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test equality constraints on associated types. Check that unsupported syntax
// does not ICE.

pub trait Foo {
    type A;
    fn boo(&self) -> <Self as Foo>::A;
}

fn foo2<I: Foo>(x: I) {
    let _: A = x.boo(); //~ ERROR cannot find type `A` in this scope
}

pub fn main() {}


