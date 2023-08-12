tests/ui/lifetimes/lifetime-errors/ex1-return-one-existing-name-return-type-is-anon.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
  field: i32
}

impl Foo {
  fn foo<'a>(&self, x: &'a i32) -> &i32 {

    x
    //~^ ERROR lifetime may not live long enough

  }

}

fn main() { }


