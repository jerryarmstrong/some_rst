tests/ui/issues/issue-8783.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
// pretty-expanded FIXME #23616

use std::default::Default;

struct X { pub x: usize }
impl Default for X {
    fn default() -> X {
        X { x: 42 }
    }
}

struct Y<T> { pub y: T }
impl<T: Default> Default for Y<T> {
    fn default() -> Y<T> {
        Y { y: Default::default() }
    }
}

fn main() {
    let X { x: _ } = Default::default();
    let Y { y: X { x } } = Default::default();
}


