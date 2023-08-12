tests/ui/regions/regions-assoc-type-static-bound-in-trait-not-met.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the compiler checks that the 'static bound declared in
// the trait must be satisfied on the impl. Issue #20890.

trait Foo {
    type Value: 'static;
    fn dummy(&self) {}
}

impl<'a> Foo for &'a i32 {
    type Value = &'a i32;
    //~^ ERROR the type `&'a i32` does not fulfill the required lifetime
}

impl<'a> Foo for i32 {
    // OK.
    type Value = i32;
}

fn main() {}


