tests/ui/issues/issue-3979-xcrate.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// aux-build:issue-3979-traits.rs

extern crate issue_3979_traits;
use issue_3979_traits::{Positioned, Movable};

struct Point { x: isize, y: isize }

impl Positioned for Point {
    fn SetX(&mut self, x: isize) {
        self.x = x;
    }
    fn X(&self) -> isize {
        self.x
    }
}

impl Movable for Point {}

pub fn main() {
    let mut p = Point{ x: 1, y: 2};
    p.translate(3);
    assert_eq!(p.X(), 4);
}


