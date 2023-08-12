tests/ui/autoref-autoderef/autoderef-method.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

trait double {
    fn double(self: Box<Self>) -> usize;
}

impl double for usize {
    fn double(self: Box<usize>) -> usize { *self * 2 }
}

pub fn main() {
    let x: Box<_> = Box::new(3);
    assert_eq!(x.double(), 6);
}


