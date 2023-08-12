tests/ui/binding/match-unique-bind.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(box_patterns)]

pub fn main() {
    match Box::new(100) {
      box x => {
        println!("{}", x);
        assert_eq!(x, 100);
      }
    }
}


