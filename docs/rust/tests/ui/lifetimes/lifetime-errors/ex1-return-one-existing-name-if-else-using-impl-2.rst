tests/ui/lifetimes/lifetime-errors/ex1-return-one-existing-name-if-else-using-impl-2.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {

fn foo<'a>(x: &i32, y: &'a i32) -> &'a i32 {
   if x > y { x } else { y } //~ ERROR explicit lifetime
   }
}

fn main() { }


