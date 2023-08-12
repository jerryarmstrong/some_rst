tests/ui/underscore-lifetime/in-binder.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we error when `'_` appears as the name of a lifetime parameter.
//
// Regression test for #52098.

struct IceCube<'a> {
    v: Vec<&'a char>
}

impl<'_> IceCube<'_> {}
//~^ ERROR `'_` cannot be used here

struct Struct<'_> {
    //~^ ERROR `'_` cannot be used here
    v: Vec<&'static char>
}

enum Enum<'_> {
    //~^ ERROR `'_` cannot be used here
    Variant
}

union Union<'_> {
    //~^ ERROR `'_` cannot be used here
    a: u32
}

trait Trait<'_> {
    //~^ ERROR `'_` cannot be used here
}

fn foo<'_>() {
    //~^ ERROR `'_` cannot be used here
}

fn main() {}


