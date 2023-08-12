tests/pretty/cast-lt.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pretty-compare-only
// pretty-mode:expanded
// pp-exact:cast-lt.pp

macro_rules! negative {
      ($e:expr) => { $e < 0 }
}

fn main() {
      negative!(1 as i32);
}


