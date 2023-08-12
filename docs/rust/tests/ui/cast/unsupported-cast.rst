tests/ui/cast/unsupported-cast.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A;

fn main() {
  println!("{:?}", 1.0 as *const A); //~ERROR  casting `f64` as `*const A` is invalid
}


