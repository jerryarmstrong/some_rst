tests/ui/lifetimes/lifetime-errors/ex3-both-anon-regions-using-fn-items.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x:fn(&u8, &u8), y: Vec<&u8>, z: &u8) {
  y.push(z);
  //~^ ERROR lifetime may not live long enough
  //~| ERROR cannot borrow
}

fn main() { }


