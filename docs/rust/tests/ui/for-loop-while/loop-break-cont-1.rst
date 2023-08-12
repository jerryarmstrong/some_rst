tests/ui/for-loop-while/loop-break-cont-1.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
  let _i = 0_usize;
  loop {
    break;
  }
  assert!(true);
}


