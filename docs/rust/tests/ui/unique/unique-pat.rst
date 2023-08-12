tests/ui/unique/unique-pat.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(box_patterns)]

fn simple() {
    match Box::new(true) {
      box true => { }
      _ => { panic!(); }
    }
}

pub fn main() {
    simple();
}


