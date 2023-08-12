tests/ui/traits/matching-lifetimes.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that the trait matching code takes lifetime parameters into account.
// (Issue #15517.)

struct Foo<'a,'b> {
    x: &'a isize,
    y: &'b isize,
}

trait Tr : Sized {
    fn foo(x: Self) {}
}

impl<'a,'b> Tr for Foo<'a,'b> {
    fn foo(x: Foo<'b,'a>) {
        //~^ ERROR method not compatible with trait
        //~^^ ERROR method not compatible with trait
    }
}

fn main(){}


