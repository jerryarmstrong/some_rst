tests/ui/closures/issue-6801.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Creating a stack closure which references a box and then
// transferring ownership of the box before invoking the stack
// closure results in a crash.



fn twice(x: Box<usize>) -> usize {
     *x * 2
}

fn invoke<F>(f: F) where F: FnOnce() -> usize {
     f();
}

fn main() {
      let x  : Box<usize>  = Box::new(9);
      let sq =  || { *x * *x };

      twice(x); //~ ERROR: cannot move out of
      invoke(sq);
}


