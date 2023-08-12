tests/ui/deref-non-pointer.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
  match *1 { //~ ERROR: cannot be dereferenced
      _ => { panic!(); }
  }
}


