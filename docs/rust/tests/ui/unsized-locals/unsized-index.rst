tests/ui/unsized-locals/unsized-index.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(unsized_fn_params)]

use std::ops;
use std::ops::Index;

pub struct A;

impl ops::Index<str> for A {
    type Output = ();
    fn index(&self, _: str) -> &Self::Output {
        &()
    }
}

impl ops::IndexMut<str> for A {
    fn index_mut(&mut self, _: str) -> &mut Self::Output {
        panic!()
    }
}

fn main() {
    let a = A {};
    let s = String::new().into_boxed_str();
    assert_eq!(&(), a.index(*s));
}


