tests/ui/resolve/name-clash-nullary.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
  let None: isize = 42; //~ ERROR mismatched types
}


