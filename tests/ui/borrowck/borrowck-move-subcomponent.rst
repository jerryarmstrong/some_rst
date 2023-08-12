tests/ui/borrowck/borrowck-move-subcomponent.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that the borrow checker checks all components of a path when moving
// out.



struct S {
  x : Box<isize>
}

fn f<T>(_: T) {}

fn main() {
  let a : S = S { x : Box::new(1) };
  let pb = &a;
  let S { x: ax } = a;  //~ ERROR cannot move out
  f(pb);
}


