tests/ui/traits/issue-6128.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::collections::HashMap;

trait Graph<Node, Edge> {
    fn f(&self, _: Edge);
    fn g(&self, _: Node);
}

impl<E> Graph<isize, E> for HashMap<isize, isize> {
    fn f(&self, _e: E) {
        panic!();
    }
    fn g(&self, _e: isize) {
        panic!();
    }
}

pub fn main() {
    let g : Box<HashMap<isize,isize>> = Box::new(HashMap::new());
    let _g2 : Box<dyn Graph<isize,isize>> = g as Box<dyn Graph<isize,isize>>;
}


