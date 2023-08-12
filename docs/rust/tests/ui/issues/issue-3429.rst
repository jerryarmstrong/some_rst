tests/ui/issues/issue-3429.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

pub fn main() {
  let x = 1_usize;
  let y = || x;
  let _z = y();
}


