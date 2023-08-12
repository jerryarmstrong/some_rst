tests/ui/loops/loop-properly-diverging-2.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn forever2() -> i32 {
  let x: i32 = loop { break }; //~ ERROR mismatched types
  x
}

fn main() {}


