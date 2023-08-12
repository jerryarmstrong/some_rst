tests/ui/issues/issue-3702.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

pub fn main() {
  trait Text {
    fn to_string(&self) -> String;
  }

  fn to_string(t: Box<dyn Text>) {
    println!("{}", (*t).to_string());
  }

}


