tests/ui/generics/single-colon-path-not-const-generics.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod foo {
    pub mod bar {
        pub struct A;
    }
}

pub struct Foo {
  a: Vec<foo::bar:A>,
  //~^ ERROR expected
  //~| HELP path separator
}

fn main() {}


