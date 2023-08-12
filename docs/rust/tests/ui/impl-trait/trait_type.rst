tests/ui/impl-trait/trait_type.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct MyType;
struct MyType2;
struct MyType3;
struct MyType4;

impl std::fmt::Display for MyType {
   fn fmt(&self, x: &str) -> () { }
   //~^ ERROR method `fmt` has an incompatible type
}

impl std::fmt::Display for MyType2 {
   fn fmt(&self) -> () { }
   //~^ ERROR method `fmt` has 1 parameter
}

impl std::fmt::Display for MyType3 {
   fn fmt() -> () { }
   //~^ ERROR method `fmt` has a `&self` declaration in the trait
}

impl std::fmt::Display for MyType4 {}
//~^ ERROR not all trait items

fn main() {}


