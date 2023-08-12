tests/ui/lifetimes/lifetime-mismatch-between-trait-and-impl.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn foo<'a>(x: &i32, y: &'a i32) -> &'a i32;
}

impl Foo for () {
    fn foo<'a>(x: &'a i32, y: &'a i32) -> &'a i32 {
    //~^ ERROR `impl` item signature doesn't match `trait` item signature
        if x > y { x } else { y }
    }
}

fn main() {}


