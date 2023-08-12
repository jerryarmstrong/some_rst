tests/ui/parser/default.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test successful and unsuccessful parsing of the `default` contextual keyword

#![feature(specialization)]
//~^ WARN the feature `specialization` is incomplete

trait Foo {
    fn foo<T: Default>() -> T;
}

impl Foo for u8 {
    default fn foo<T: Default>() -> T {
        T::default()
    }
}

impl Foo for u16 {
    pub default fn foo<T: Default>() -> T { //~ ERROR unnecessary visibility qualifier
        T::default()
    }
}

impl Foo for u32 { //~ ERROR not all trait items implemented, missing: `foo`
    default pub fn foo<T: Default>() -> T { T::default() }
    //~^ ERROR `default` is not followed by an item
    //~| ERROR non-item in item list
}

fn main() {}


