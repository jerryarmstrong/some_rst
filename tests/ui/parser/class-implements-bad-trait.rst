tests/ui/parser/class-implements-bad-trait.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:nonexistent
class cat : nonexistent {
  let meows: usize;
  new(in_x : usize) { self.meows = in_x; }
}

fn main() {
  let nyan = cat(0);
}


