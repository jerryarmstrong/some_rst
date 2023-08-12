tests/ui/binding/match-naked-record-expr.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

struct X { x: isize }

pub fn main() {
    let _x = match 0 {
      _ => X {
        x: 0
      }.x
    };
}


