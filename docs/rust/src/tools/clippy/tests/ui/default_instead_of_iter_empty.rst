src/tools/clippy/tests/ui/default_instead_of_iter_empty.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![warn(clippy::default_instead_of_iter_empty)]
#![allow(dead_code)]
use std::collections::HashMap;

#[derive(Default)]
struct Iter {
    iter: std::iter::Empty<usize>,
}

fn main() {
    // Do lint.
    let _ = std::iter::Empty::<usize>::default();
    let _ = std::iter::Empty::<HashMap<usize, usize>>::default();
    let _foo: std::iter::Empty<usize> = std::iter::Empty::default();

    // Do not lint.
    let _ = Vec::<usize>::default();
    let _ = String::default();
    let _ = Iter::default();
}


