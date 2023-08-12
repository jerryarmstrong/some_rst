tests/ui/issues/issue-5280.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

type FontTableTag = u32;

trait FontTableTagConversions {
  fn tag_to_string(self);
}

impl FontTableTagConversions for FontTableTag {
  fn tag_to_string(self) {
      let _ = &self;
  }
}

pub fn main() {
    5.tag_to_string();
}


