tests/ui/binding/match-naked-record.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

struct X { x: isize }

pub fn main() {
    let _x = match 0 {
      _ => X {
        x: 0
      }
    };
}


