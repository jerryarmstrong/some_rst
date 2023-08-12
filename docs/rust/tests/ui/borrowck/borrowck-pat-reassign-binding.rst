tests/ui/borrowck/borrowck-pat-reassign-binding.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut x: Option<isize> = None;
    match x {
      None => {
          // Note: on this branch, no borrow has occurred.
          x = Some(0);
      }
      Some(ref i) => {
          // But on this branch, `i` is an outstanding borrow
          x = Some(*i+1); //~ ERROR cannot assign to `x` because it is borrowed
          drop(i);
      }
    }
    x.clone(); // just to prevent liveness warnings
}


