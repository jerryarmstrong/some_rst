tests/ui/binding/match-ref-binding.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn destructure(x: Option<isize>) -> isize {
    match x {
      None => 0,
      Some(ref v) => *v
    }
}

pub fn main() {
    assert_eq!(destructure(Some(22)), 22);
}


