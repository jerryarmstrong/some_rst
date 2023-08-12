tests/ui/lifetimes/lifetime-errors/ex1-return-one-existing-name-if-else-using-impl-3.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
  field: i32
}

impl Foo {
  fn foo<'a>(&'a self, x: &i32) -> &i32 {

    if true { &self.field } else { x } //~ ERROR explicit lifetime

  }

}

fn main() { }


